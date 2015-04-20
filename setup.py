#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re
import os
import sys

root_package_dir = '.'

name = 'english-filters'
package = 'english_filters'
description = 'Django template filters for working with English text'
url = 'http://github.com/brightinteractive/english-filters/'
author = 'Bright Interactive'
author_email = 'francis@bright-interactive.com'
license = 'BSD'
install_requires = ['Django>=1.4,<1.7']
packages = find_packages(root_package_dir)


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(root_package_dir, package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)

script_args = sys.argv[1:]
display_tag_message = False

if script_args and script_args[-1] == 'publish':
    script_args[-1:] = ['sdist', 'upload']
    display_tag_message = True


setup(
    name=name,
    version=get_version(package),
    url=url,
    license=license,
    description=description,
    author=author,
    author_email=author_email,
    packages=packages,
    package_dir={'': root_package_dir},
    install_requires=install_requires,
    script_args=script_args,
    include_package_data=True
)

if display_tag_message:
    args = {'version': get_version(package)}
    print "You probably want to also tag the version now:"
    print "  git tag -a v%(version)s -m 'Version %(version)s'" % args
    print "  git push --tags"
