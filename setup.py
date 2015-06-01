# Copyright (C) 2014 pyeasy
# Author: WeizhongTu
# All rights reserved.
# MIT license

from setuptools import setup, find_packages

setup(
    name='excel',
    version='1.0.0',
    author='Weizhong Tu',
    author_email='tuweizhong@163.com',
    packages=find_packages(),

    license='MIT',
    install_requires=[
        'xlrd',
    ],
 )
