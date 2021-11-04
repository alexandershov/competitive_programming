from setuptools import find_packages
from setuptools import setup

setup(
    author='Alexander Ershov',
    package_dir={'': 'src'},
    packages=find_packages(),
    tests_require=['pytest'],
)

