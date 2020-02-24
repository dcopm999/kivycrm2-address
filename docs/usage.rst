=====
Usage
=====

To use Address book application for KivyCRM v2 in a project, add it to your `INSTALLED_APPS`:

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
