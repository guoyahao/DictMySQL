#!/usr/bin/python
# -*-coding: utf-8 -*-

from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

setup(name='dictmysql',

      version='0.4.10',

      description='A mysql class for more convenient database manipulations with Python dictionary.',

      author='Guangyang Li',

      author_email='mail@guangyangli.com',

      license='MIT',

      py_modules=['dictmysql'],

      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5'
      ],

      keywords='python mysql class',

      url='https://ligyxy.github.io/DictMySQL/',

      install_requires=["PyMySQL>=0.7"],
      )
