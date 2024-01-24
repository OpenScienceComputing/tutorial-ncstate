#!/usr/bin/env python
# coding: utf-8

# # Calculate keepbits for CNAPSv2 daily average files with 99.9% info
# snip out a piece of water only and determine keepbits for CNAPS vars using xinfo, using a water only subset

# In[1]:


import xarray as xr
import xbitinfo as xb
import fsspec
from pathlib import Path


# In[2]:


fs = fsspec.filesystem('file')


# In[3]:


flist = fs.glob('/storage/cnapsv2/useast_avg_*.nc')


# In[4]:


ds = xr.open_dataset(flist[0], chunks={'ocean_time':1}, drop_variables=['dstart'])


# In[5]:


# calculate keepbits on a section with water cells only, and only for first 10 time steps


# In[6]:


ds2 = ds[['temp','salt','omega','zeta']].isel(ocean_time=slice(0,10), s_rho=-1, s_w=-4,
               eta_rho=slice(500,700), xi_rho=slice(800,1000))
bitinfo = xb.get_bitinformation(ds2, dim="xi_rho", implementation='python')
keepbits1 = xb.get_keepbits(bitinfo, inflevel=0.999)  # get number of mantissa bits to keep for 99% real information
keepbits1.values


# In[7]:


ds2 = ds[['v','vbar']].isel(ocean_time=slice(0,100), s_rho=-1,
               eta_v=slice(500,700), xi_v=slice(800,1000))
bitinfo = xb.get_bitinformation(ds2, dim="xi_v", implementation='python')
keepbits2 = xb.get_keepbits(bitinfo, inflevel=0.999)  # get number of mantissa bits to keep for 99% real information
keepbits2.values


# In[8]:


ds2 = ds[['u','ubar']].isel(ocean_time=slice(0,100), s_rho=-1,
               eta_u=slice(500,700), xi_u=slice(800,1000))
bitinfo = xb.get_bitinformation(ds2, dim="xi_u", implementation='python')
keepbits3 = xb.get_keepbits(bitinfo, inflevel=0.999)  # get number of mantissa bits to keep for 99% real information
keepbits3.values


# In[9]:


keepbits = xr.merge([keepbits1, keepbits2, keepbits3], compat='override')


# In[10]:


keepbits.to_netcdf('keepbits.nc', mode='w')

