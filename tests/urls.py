# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from dj_bootstrap_swatches.urls import urlpatterns as dj_bootstrap_swatches_urls

urlpatterns = [
    url(r'^', include(dj_bootstrap_swatches_urls, namespace='dj_bootstrap_swatches')),
]
