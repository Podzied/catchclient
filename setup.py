from setuptools import setup, find_packages

setup(
    name='catchclient',
    version='1.0.0',
    url='https://github.com/podzied/catchclient',
    author='Podzied',
    description='Email Catch-All Client and API Wrapper for emailfake.com',
    packages=find_packages(),    
    install_requires=['requests >= 2.28.1', 'bs4 >= 0.0.1', 'retrying >= 1.3.3'],
)
