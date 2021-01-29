#!/usr/bin/env python

import setuptools
import unittest

pkg_name = 'whatever'

setuptools.setup(name='whatever',
    version='0.0.1',
    description='Whatever description',
    author='Luis Carlos Garcia Peraza Herrera',
    author_email='luiscarlos.gph@gmail.com',
    license='MIT',
    packages=[
        pkg_name, 
        pkg_name + '.models', 
        pkg_name + '.views', 
        pkg_name + '.controllers'
    ],
    package_dir={
        pkg_name: 'src/' + pkg_name, 
        pkg_name + '.models': 'src/' + pkg_name + '/models',
        pkg_name + '.views': 'src/' + pkg_name + '/views', 
        pkg_name + '.controllers': 'src/' + pkg_name + '/controllers',
    },
    test_suite='tests',
    include_package_data=True,
)
