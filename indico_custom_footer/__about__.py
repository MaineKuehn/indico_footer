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
"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
``indico_custom_footer`` - Footer Customisation Plugin for Indico
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. image:: https://readthedocs.org/projects/indico_footer/badge/?version=latest
    :target: http://indico-footer.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation

.. image: https://img.shields.io/pypi/v/indico_footer.svg
    :alt: Available on PyPI
    :target: https://pypi.python.org/pypi/indico_footer/

.. image:: https://img.shields.io/github/license/MaineKuehn/indico_footer.svg
    :alt: License
    :target: https://github.com/MaineKuehn/indico_footer/blob/master/LICENSE

Plugin for the Indico event management system to customise the footer.
For detailed information, see also the `official documentation <http://indico-footer.readthedocs.io/en/latest/>`_.

Quick Guide
-----------

To enable the plugin, it must be installed for the python version running ``indico``.

.. code:: bash

    python -m pip install indico-plugin-custom-footer

Once installed, it can be enabled in the Indico configuration.
New footer elements can be added by configuring the plugin in the administrator settings.

Disclaimer
----------

This plugin is in no way endorsed, supported or provided by Indico or any other service, provider or entity.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, ORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
__title__ = 'indico-plugin-custom-footer'
__summary__ = 'Indico Footer Customisation Plugin'
__url__ = 'https://github.com/MaineKuehn/indico_footer'

__version__ = '2.0.0'
__author__ = 'Eileen Kuehn, Max Fischer'
__email__ = 'eileen.kuehn@kit.edu'
__copyright__ = '2018 %s' % __author__
__keywords__ = 'indico customisation footer html plugin'
