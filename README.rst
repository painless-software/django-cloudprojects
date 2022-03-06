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

    $ pip install django-cloudprojects

Basic Usage
===========

1. Add ``cloudprojects`` to your Django project settings, e.g.

.. code:: python

    INSTALLED_APPS = [
        ...
        'cloudprojects',
    ]

2. Add ``cloudprojects`` to your project ``urls`` module, e.g.

.. code:: python

    urlpatterns = [
        url('', cloudprojects.urls),
        ...
    ]
