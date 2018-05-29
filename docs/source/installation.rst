Installation
============

The plugin can be installed using standard Python package managers.
To enable the plugin, it must be added to the configuration file of indico.

Note that at least ``indico`` 2.0 is required, and will be installed automatically if it is missing.

Installing the package
----------------------

The ``indico_footer`` plugin must be installed for the python version running ``indico``.
With a standard indico installation, you must activate the indico python virtual environment first.

.. code:: bash

    su - indico
    source ~/.venv/bin/activate

The latest release version is available for the default python package managers.
You can directly install the module using ``pip``:

.. code:: bash

    pip install indico_footer

This can also be used to upgrade to a newer version:

.. code:: bash

    pip install indico_footer --upgrade

Enabling the package
--------------------

All plugins must be enabled in indico's configuration file.
By default, the configuration is located in ``/opt/indico/etc/indico.conf``.

.. code:: python

    PLUGINS = {'custom_footer'}

Note that if you need multiple plugins, you must include them all in the set of ``PLUGINS``:

.. code:: python

    PLUGINS = {'payment_manual', 'payment_paypal', 'payment_sixpay', 'custom_footer'}
