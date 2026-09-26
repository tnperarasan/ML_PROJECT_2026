'''
 This setup.py will be the responsible in creating the Machine Learnig application as a package
 and we can deploy this in pypi and from there anybody can do the installation and anybody can also
 use it.
 
 But when you are creating a proper Python package, setup.py gives your project package metadata and installation configuration.
 "This folder is a Python project/package, and here is its information and dependencies."
'''
from setuptools import find_packages,setup
from typing import List
 
 ### "This folder is a Python project/package, and here is its information and dependencies."
 
def get_requirements(file_path:str)->List[str] : 
    '''
        This functoin returns List of requirments
    
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != "-e ."]
    return requirements
   
setup(
    name= "ML_Project",  ## PROJECT NAME 
    version= "0.0.1",     ## PROJECT VERSION
    author= "Perarasan",
    author_email= "tnperarasan@gmail.com",
    packages=find_packages(),                   ##PYTHON PACKAGES INSIDE THE PROJECT 
    install_requires=get_requirements('requirements.txt') ## PYTHON PACKAGES REQUIRED BY THE PROJECT 
     
)
### find_packages()
##searches for Python packages, generally directories containing: __init__.py 
# and tells setuptools which packages should be included.