.. indico_footer documentation master file, created by
   sphinx-quickstart on Mon May 28 21:45:19 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===================================================
``indico_footer`` - Footer Customisation for Indico
===================================================

.. image:: https://readthedocs.org/projects/indico_footer/badge/?version=latest
    :target: http://indico_footer.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation

.. image:: https://img.shields.io/pypi/v/indico_footer.svg
    :alt: Available on PyPI
    :target: https://pypi.python.org/pypi/indico_footer/

.. image:: https://img.shields.io/github/license/MaineKuehn/indico_footer.svg
    :alt: License
    :target: https://github.com/MaineKuehn/indico_footer/blob/master/LICENSE

.. image:: https://img.shields.io/github/commits-since/MaineKuehn/indico_footer/v2.0.1.svg
    :alt: Repository
    :target: https://github.com/MaineKuehn/indico_footer/tree/master

.. toctree::
    :maxdepth: 1
    :caption: Subtopics Overview:

    source/installation
    source/changelog

The :py:mod:`indico_footer` allows you to add custom links to the Indico footer.

Overview
--------

If the plugin is enabled, administrators can add additional links to the Indico footer.
For example, in addition to the ``Terms and conditions``
you can now add a ``legal disclaimers`` link to your organization's disclaimers.

Once :doc:`installed <source/installation>`, the administrator panel allows adding new footer links.
Each link consists of the following settings:

**Name**
   The link name as shown in the footer.

**Link**
   The address as pointed to by the link.

**Target**
   Where to open the link: ``_self`` for the current window or ``_blank`` for a new window/tab.

Quick Guide
-----------

To enable the plugin, it must be installed for the python version running ``indico``.

.. code:: bash

    python -m pip install indico_footer

Once installed, it can be enabled in the Indico configuration.
New footer elements can be added by configuring the plugin in the administrator settings.

Contributing and Feedback
-------------------------

The project is hosted on `github <https://github.com/MaineKuehn/indico_footer>`_.
Feedback, pull requests and other contributions are always welcome.
If you have issues or suggestions, check the issue tracker: |issues|

Disclaimer
----------

This plugin is in no way endorsed, supported or provided by Indico or any other service, provider or entity.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

----------

.. |issues| image:: https://img.shields.io/github/issues-raw/MaineKuehn/indico_footer.svg
   :target: https://github.com/MaineKuehn/indico_footer/issues
   :alt: Open Issues

Documentation built from ``indico_footer`` |version| at |today|.
