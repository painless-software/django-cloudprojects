"""
Initialize authentication providers.
"""
import os

from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Configure authentication providers in the database.
    """

    def handle(self, *labels, **options):
        """
        Configure OAuth2 authentication providers.
        """
        social_auth_providers = [
            ('bitbucket', 'Bitbucket'),
            ('github', 'GitHub'),
            ('gitlab', 'GitLab'),
        ]
        count = 0

        site, created = Site.objects.get_or_create(id=1)
        site.name = 'Example'
        site.domain = 'example.com'
        site.save()

        for provider, name in social_auth_providers:
            app_config, created = SocialApp.objects.get_or_create(
                provider=provider, name=name)
            if not created:
                self.stdout.write(f'App configuration already exists: {name}'
                                  ' -- leaving it untouched.')
            else:
                PROVIDER = provider.upper()
                app_secret = os.getenv(f'{PROVIDER}_APPSECRET', '<?>')
                app_key = os.getenv(f'{PROVIDER}_APPKEY', '<?>')
                app_config.client_id = provider
                app_config.secret = app_secret
                app_config.key = app_key
                app_config.save()
                count += 1

        total = SocialApp.objects.count()
        self.stdout.write(f'{count} SocialAuth apps configured, '
                          f'{total} in total.')
