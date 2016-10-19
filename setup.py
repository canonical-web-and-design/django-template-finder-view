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
    version='0.3',
    url='',
    license='LGPLv3',
    author='Canonical Webteam',
    description='A view for automatically finding and rendering Django templates',
    packages=['django_template_finder_view'],
    include_package_data=True,
    platforms='any',
    install_requires=[
        "Django >= 1.3",
    ],
)
