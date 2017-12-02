#!/usr/bin/env python
from setuptools import setup, find_packages
from admin_log_entries import __version__

setup(
    name='django-adminlogentries',
    version=__version__,
    description=(
        'A Django app that provides a ModelAdmin for django.contrib.admin\'s '
        'LogEntry model (with everything except the list disabled)'
    ),
    author='Adam Taylor',
    author_email='ataylor32@gmail.com',
    url='https://github.com/ataylor32/django-adminlogentries',
    packages=find_packages(),
    include_package_data=True,
)
