import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='django-keen',
    version='0.1.0',
    author='Jannis Gebauer',
    author_email='',
    packages=['dkeen',],
    url='http://pypi.python.org/pypi/django-keen/',
    license='LICENSE.txt',
    description='',
    long_description=open('README.txt').read(),
    install_requires=required
)