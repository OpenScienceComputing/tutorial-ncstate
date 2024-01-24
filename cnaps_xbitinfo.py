#!/usr/bin/env python
# coding: utf-8

# # Test compressing CNAPSv2 daily average files with 99.9% info
# snip out a piece of water only and determine keepbits for CNAPS vars using xinfo, using a water only subset

# In[1]:


import xarray as xr
import xbitinfo as xb
import hvplot.xarray
import fsspec
import zarr
from pathlib import Path


# In[2]:


fs = fsspec.filesystem('file')


# In[8]:


flist = fs.glob('/storage/cnapsv2/useast_avg_*.nc')
keepbits_file = 'keepbits.nc'


# In[ ]:


for f in flist:
    fname = Path(f).stem
    zarr_out = f'/storage/xbitinfo/{fname}_999.zarr'
    if not Path(zarr_out).is_dir():    # Don't write already completed years
        print(f'creating {zarr_out}')
        ds = xr.open_dataset(f, chunks={'ocean_time':1}, drop_variables=['dstart'])
        keepbits = xr.open_dataset(keepbits_file)    # read keepbits from file
        vnames = [v for v in keepbits.data_vars]
        ds_bitrounded = xb.xr_bitround(ds[vnames], keepbits)  # bitrounding keeping only keepbits mantissa bits
        ds_bitrounded.to_compressed_zarr(zarr_out, mode='w')  # save to zarr with compression
        ds_static = ds.drop_vars(vnames)
        ds_static.to_zarr(zarr_out, mode='a')
        zarr.consolidate_metadata(zarr_out)


# In[ ]:




