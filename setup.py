# -*- coding: utf-8 -*-
#
# This file is part of the Indico Footer Customisation Plugin.
# Copyright (C) 2018 Eileen Kuehn, Max Fischer
#
# This is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Indico Footer Customisation Plugin;if not, see <http://www.gnu.org/licenses/>.
import os
from setuptools import setup, find_packages

repo_base_dir = os.path.abspath(os.path.dirname(__file__))
# pull in the packages metadata
package_about = {}
with open(os.path.join(repo_base_dir, "indico_custom_footer", "__about__.py")) as about_file:
    exec(about_file.read(), package_about)

setup(
    name=package_about['__title__'],
    version=package_about['__version__'],
    description=package_about['__summary__'],
    long_description=package_about['__doc__'].strip(),
    author=package_about['__author__'],
    author_email=package_about['__email__'],
    url=package_about['__url__'],
    entry_points={
        'indico.plugins': {
            'custom_footer = indico_custom_footer.plugin:FooterCustomisationPlugin'
        }
    },
    packages=find_packages(),
    install_requires=['indico>=2.0'],
    license='GPLv3+',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Communications :: Conferencing',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    zip_safe=True,
    keywords=package_about['__keywords__'],
)
