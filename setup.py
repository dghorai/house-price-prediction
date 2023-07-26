# import modules
import sys

class VersionError(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    from setuptools import find_packages, setup
except ImportError:
    raise("Please install setuptools to run setup.py")

from typing import List


def readme():
    with open('README.md') as f:
        return f.read()

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    return requirements

setup(
    name='LinearRegressionProject',
    version='0.0.1',
    description='Boston house price prediction using linear regression model',
    author='Debabrata Ghorai, Ph.D.',
    author_email='ghoraideb@gmail.com',
    url='https://github.com/dghorai83',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages(),
    long_description=readme()
)