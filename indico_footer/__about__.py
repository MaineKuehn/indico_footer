"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
``indico_footer`` - Footer Customisation Plugin for Indico
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

    python -m pip install indico_footer

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
__title__ = 'indico_footer'
__summary__ = 'Indico Footer Customisation Plugin'
__url__ = 'https://github.com/MaineKuehn/indico_footer'

__version__ = '1.0.0'
__author__ = 'Eileen Kuehn, Max Fischer'
__email__ = 'eileen.kuehn@kit.edu'
__copyright__ = '2018 %s' % __author__
__keywords__ = 'indico customisation footer html plugin'
