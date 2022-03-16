"""
URL configuration for django-cloudprojects.
"""

from django.conf import settings
from django.urls import include, path

urlpatterns = []

if 'django_saml' in settings.INSTALLED_APPS:
    urlpatterns = [
        path('saml/', include('django_saml.urls')),
    ]

urlpatterns += [
    path('', include('allauth.urls')),
]
