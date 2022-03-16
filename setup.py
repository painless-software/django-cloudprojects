"""
Packaging setup for the django-cloudprojects Python package.
"""
from pathlib import Path

from setuptools import find_packages, setup

import cloudprojects as package


def read_file(filename):
    """Read a text file and return its contents."""
    project_home = Path(__file__).parent.resolve()
    file_path = project_home / filename
    return file_path.read_text(encoding="utf-8")


setup(
    name='django-cloudprojects',
    version=package.__version__,
    author='Peter Bittner',
    author_email='django@bittner.it',
    description=package.__doc__.strip(),
    long_description=read_file('README.rst'),
    long_description_content_type='text/x-rst',
    url='https://github.com/painless-software/django-cloudprojects',
    packages=find_packages(exclude=['test*']),
    keywords=[
        'cloud',
        'kubernetes',
        'openshift',
        'django',
        'software',
        'development',
        'hosting',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    extras_require={
        'saml': ['python3-saml-django'],
    },
    install_requires=[
        'django-allauth',
    ],
    python_requires='>=3.6',
)
