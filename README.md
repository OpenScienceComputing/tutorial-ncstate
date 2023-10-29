# Materials for 2023-CSDMS Clinic 1.2: 
"Emerging open-source Python-based infrastructure for scalable, data-proximate analysis and visualization of model output (a.k.a. the Pangeo Framework)"

## Start
1. login to https://nebari-workshop.esipfed.org:
   ```
   username: <your email address>
   password: 123  (you will be prompted to change it)
   ```
1. Start a "regular instance" server (the default).  This launches JupyterLab.     
1. In the JupyterLab interface, open a terminal ("File"->"New"->"Terminal")
    
1. In the terminal, type:
    ``` shell
    cd /shared/users
    python start.py
    ```
1. In the file browser, browse to the 'shared'->'users' and then your username folder. 
1. Browse to "training-2023-CSDMS"
1. Click the "clinic_overview.ipynb" notebook to launch it. 

## Deployment notes
1. Deployed Nebari 2023.5.1 on AWS using username/password for authentication
2. In Keycloak, added a `users` group, with same permissions as `analyst` (allowing dask gateway cluster creation). To do this go to the `users` group, select Role Mapping, at the bottom of that page is a Client Roles drop down that you can use to add and remove roles for that group.  Add `dask-developer`. 
4. We created a CSV list of users with columns: first_name, last_name, email
5. Converted the CSV to a JSON file importable into keycloak using `generate_keycloak.ipynb` in this repo

5. At the time of the May 13 workshop, destroying on AWS with `nebari destroy` didn't everything:
  ```
  [terraform]: Destroy complete! Resources: 2 destroyed.
[terraform]: Stage=stages/07-kubernetes-services failed to fully destroy
Stage=stages/05-kubernetes-keycloak failed to fully destroy
Stage=stages/04-kubernetes-ingress failed to fully destroy
Stage=stages/03-kubernetes-initialize failed to fully destroy
Stage=stages/02-infrastructure failed to fully destroy
ERROR: not all nebari stages were destroyed properly. For cloud deployments of Nebari typically only stages 01 and 02 need to succeed to properly destroy everything
  ```
[This AWS force destroy script](https://github.com/nebari-dev/nebari/blob/develop/scripts/aws-force-destroy.sh) from @iameskild should destroy everything, but be careful, as it destroys the current cluster, which may not be the cluster you indended if the `nebari destroy` already destroyed the targeted cluster!
# tutorial-ncstate
