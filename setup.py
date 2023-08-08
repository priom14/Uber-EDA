from setuptools import find_packages, setup
from typing import List

Hyphen_e_dot = '-e .'

def get_requirs(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements ]

        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)

setup(
name='Uber EDA',
version='0.0.1',
author='Priom Pal',
author_email='priompalnfs@yahoo.com',
packages=find_packages(),
install_requires = get_requirs('requirments.txt')
)