#!/bin/python
import os
import subprocess

#use first part of email address as username
hub_user = os.environ['JUPYTERHUB_USER']
username = hub_user.split('@')[0]

# create shared folder for user
my_shared_folder = f'/shared/users/{username}'

if not os.path.exists(my_shared_folder):
    os.makedirs(my_shared_folder)
    print(f'{my_shared_folder} created!')
else:
    print(f'{my_shared_folder} exists!')

# change directory to shared folder
os.chdir(my_shared_folder)

# clone training material
try:
    subprocess.run(["git", "clone", "https://github.com/OpenScienceComputing/tutorial-ncstate.git"])
    print('cloned tutorial repository!')
except:
    print('failed to clone tutorial repository')

# copy kerchunk tutorial (and any other repos in /shared/users/repos) 
try:
    subprocess.run(["cp", "-R", "/shared/users/repos", "."])
    print(f'copied repos to {my_shared_folder}')
except:
    print(f'failed to copy repos to {my_shared_folder}')

# copy bucket credentials
try:
    subprocess.run(["cp", "-R", "/shared/users/.aws", f'/home/{hub_user}/'])
    print('copied cloud credentials')
except:
    print('failed to copy cloud credentials')
