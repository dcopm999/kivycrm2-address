=============================
Address book application for KivyCRM v2
=============================

.. image:: https://badge.fury.io/py/kivycrm2-address.svg
    :target: https://badge.fury.io/py/kivycrm2-address

.. image:: https://travis-ci.org/dcopm999/kivycrm2-address.svg?branch=master
    :target: https://travis-ci.org/dcopm999/kivycrm2-address

.. image:: https://codecov.io/gh/dcopm999/kivycrm2-address/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dcopm999/kivycrm2-address

Address book application for KivyCRM v2

Documentation
-------------

The full documentation is at https://kivycrm2-address.readthedocs.io.

Quickstart
----------

Install Address book application for KivyCRM v2::

    pip install kivycrm2-address

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'address.apps.AddressConfig',
        ...
    )

Add Address book application for KivyCRM v2's URL patterns:

.. code-block:: python

    from address import urls as address_urls


    urlpatterns = [
        ...
        url(r'^', include(address_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
