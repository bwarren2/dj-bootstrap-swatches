=====
Usage
=====

To use Django Bootstrap Swatches in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_bootstrap_swatches.apps.DjBootstrapSwatchesConfig',
        ...
    )

Add Django Bootstrap Swatches's URL patterns:

.. code-block:: python

    from dj_bootstrap_swatches import urls as dj_bootstrap_swatches_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_bootstrap_swatches_urls)),
        ...
    ]
