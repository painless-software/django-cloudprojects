"""
URL configuration for django-cloudprojects.
"""

from django.urls import include, path

urlpatterns = []

try:
    import django_saml

    urlpatterns = [
        path('saml/', django_saml.urls),
    ]
except ImportError:
    pass

urlpatterns += [
    path('', include('allauth.urls')),
]
