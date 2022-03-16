"""
Unit tests for cloudprojects urls.
"""

import pytest
from django.conf import settings


@pytest.mark.skipif('django_saml' not in settings.INSTALLED_APPS,
                    reason="requires python3-saml-django installed")
@pytest.mark.django_db
def test_saml_login(client):
    """
    A SAML login attempt redirects to a SAML SSO resource.
    """
    expected_redirect = 'https://example.com/trust/saml2/http-post/sso/?SAMLRequest='

    response = client.get('/saml/login', HTTP_HOST='example.com')

    assert response.status_code == 302
    assert response.url.startswith(expected_redirect)


@pytest.mark.django_db
def test_allauth_login(client):
    """
    A (social) login attempt shows the Allauth login page.
    """
    response = client.get('/login/', HTTP_HOST='example.com')

    assert response.status_code == 200
    assert b'<h1>Sign In</h1>' in response.content
    assert b'/bitbucket_oauth2/login/?process=login">Bitbucket</a>' in response.content
    assert b'/github/login/?process=login">GitHub</a>' in response.content
    assert b'/gitlab/login/?process=login">GitLab</a>' in response.content
