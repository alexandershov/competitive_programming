from setuptools import find_packages
from setuptools import setup

setup(
    author='Alexander Ershov',
    name='competitive_programming',
    package_dir={'': 'src'},
    packages=find_packages(),
    python_requires='>=3.10',
    tests_require=['pytest'],
    version='0.0.1',
)
