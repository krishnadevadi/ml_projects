# setup.py is responsible for creating the current machine learning application as a package, we use the package for
# many reasons like deployment and all

from setuptools import find_packages, setup
# find pacakages will be used to identify all the packages we are using in the current ML application

from typing import List


def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n", '') for req in requirements]
        '''
        This function returns the list of requirements
        '''
        if "-e." in requirements:
            requirements.remove("-e.")
        return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Venu",
    author_email="venugopal.edu2022@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

# setup.py how is it able to identify how many packages are there??

# for this we are going to create a new folder src and in that we are going to write __init__py,
# the find_packages is going to check where we got __init__py and, it considers the source as package itself and
# once its is built we can then import it where we want like how we import packages

# when we have situations where we have soo many packages and we cannot mention each and every package name manually,
# in that case we create a function to retrieve the packages installed --> install_requires = ['pandas','numpy','seaborn']
