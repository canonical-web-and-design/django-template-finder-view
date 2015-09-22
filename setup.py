# -*- coding: utf-8 -*-
"""
Django template finder view
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='django-template-finder-view',
    version='0.1',
    url='',
    license='LGPLv3',
    author='Robin',
    description='A view for automatically finding and rendering Django templates',
    packages=['template_finder_view'],
    include_package_data=True,
    platforms='any',
    install_requires=[
        "Django >= 1.3",
    ],
)

