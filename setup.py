#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='port_supervisor',
      scripts=['port_supervisor'],
      packages=find_packages(),
      install_requires=['paramiko']
)
