Cloud Projects for Django |latest-version|
==========================================

|checks-status| |tests-status| |python-support| |license|

A pluggable Django web application for onboarding and managing applications
and microservices on cloud platforms, the DevOps (DevSecOps) way.


.. |latest-version| image:: https://img.shields.io/pypi/v/django-cloudprojects.svg
   :alt: Latest version on PyPI
   :target: https://pypi.org/project/django-cloudprojects
.. |checks-status| image:: https://img.shields.io/github/workflow/status/painless-software/django-cloudprojects/Checks/main?label=Checks&logo=github
   :alt: GitHub Workflow Status
   :target: https://github.com/painless-software/django-cloudprojects/actions/workflows/check.yml
.. |tests-status| image:: https://img.shields.io/github/workflow/status/painless-software/django-cloudprojects/Tests/main?label=Tests&logo=github
   :alt: GitHub Workflow Status
   :target: https://github.com/painless-software/django-cloudprojects/actions/workflows/test.yml
.. |python-support| image:: https://img.shields.io/pypi/pyversions/django-cloudprojects.svg
   :alt: Python versions
   :target: https://pypi.org/project/django-cloudprojects
.. |license| image:: https://img.shields.io/pypi/l/django-cloudprojects.svg
   :alt: Software license
   :target: https://github.com/painless-software/django-cloudprojects/blob/main/LICENSE


Who Should Use This Application
-------------------------------

Any sufficiently large organization runs a significant amount of software on
modern cloud infrastructure nowadays, either in public clouds or on premise,
in a private cloud.
Onboarding this software, typically microservice or monolithic applications,
is far from trivial though, especially on premise or with hybrid clouds.
Unlike public clouds, which usually have onboarding processes well-defined
for single applications, corporate environments run highly custom processes.

*Cloud Projects* allows organizations to build a self-service infrastructure
that can be used by system engineers to automate parts of their usually manual
onboarding activities and monitor the progress of those slow-moving activities.
Mature agile organizations can even allow software development agencies to
service themselves entirely and request corporate project management, DevOps
and security specialists to support their engineering workforce through
*Cloud Projects*.

Features
--------

- Mature software development capabilities (Django Web framework)
- Pluggable infrastructure for flexible application development (Django apps)
- Usable defaults and easy configuration (Django settings)

Installation
============

The easiest way to install *django-cloudprojects* is with pip:

.. code:: console

    pip install django-cloudprojects

SAML support is available as an installation option:

.. code:: console

    pip install django-cloudprojects[saml]

Note that SAML support requires additional libraries installed on your target
system, e.g. for Debian/Ubuntu- and RedHat/CentOS-based systems:

.. code:: console

   sudo apt-get install libxml2-dev libxmlsec1-dev libxmlsec1-openssl

.. code:: console

   sudo yum install libxml2-devel xmlsec1-devel xmlsec1-openssl-devel libtool-ltdl-devel

Basic Usage
===========

1. In your Django project settings, add ``cloudprojects`` and its dependencies
   to ``INSTALLED_APPS``, optionally omitting the authentication providers you
   don't intend to use, add the required authentication backends for Allauth
   and the Django Admin, and make sure ``SITE_ID`` is defined, e.g.

.. code:: python

    INSTALLED_APPS = [
        'django.contrib.auth',
        'django.contrib.messages',
        'django.contrib.sites',
        ...
        # 'django_saml',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        # 'allauth.socialaccount.providers.bitbucket_oauth2',
        # 'allauth.socialaccount.providers.github',
        'allauth.socialaccount.providers.gitlab',
        'cloudprojects',
    ]

    AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.ModelBackend',
        'django_saml.backends.SamlUserBackend',
        'allauth.account.auth_backends.AuthenticationBackend',
    ]

    SITE_ID = 1

2. Add ``cloudprojects`` to your project's ``urls`` module, e.g.

.. code:: python

    urlpatterns = [
        ...
        path('', include('cloudprojects.urls')),
    ]

3. In your Django project settings, configure the authentication providers as
   described in the `Allauth documentation`_, e.g.

.. code:: python

    SOCIALACCOUNT_PROVIDERS = {
        'github': {
            'GITHUB_URL': 'https://github.enterprise.local',
            'SCOPE': ['api'],
        },
        'gitlab': {
            'GITLAB_URL': 'https://gitlab.selfhosted.local',
            'SCOPE': ['api'],
        },
    }

4. Register the authentication apps with your VCS services as described in the
   Allauth documentation:

   - `Bitbucket provider`_
   - `GitHub provider`_
   - `GitLab provider`_

   We recommend writing a management command to automatically configure those
   values during deployment.  See our `test project`_ for a suggestion on how
   an implementation may look like.

5. If you intend to use SAML you need to add all required settings to your
   project's Django settings, as described in the `python3-saml-django docs`_.


.. _Allauth documentation:
    https://django-allauth.readthedocs.io/en/latest/providers.html
.. _GitHub provider:
    https://django-allauth.readthedocs.io/en/latest/providers.html#github
.. _GitLab provider:
    https://django-allauth.readthedocs.io/en/latest/providers.html#gitlab
.. _Bitbucket provider:
    https://django-allauth.readthedocs.io/en/latest/providers.html#bitbucket
.. _test project:
    https://github.com/painless-software/django-cloudprojects/tree/main/tests/testproject
.. _python3-saml-django docs:
    https://pypi.org/project/python3-saml-django/
