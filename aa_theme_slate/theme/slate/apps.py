"""
AppConfig for Alliance Auth Slate theme.
"""

# Django
from django.apps import AppConfig


class AaSlateThemeConfig(AppConfig):
    """
    AppConfig for Alliance Auth Slate theme.
    """

    name = "aa_theme_slate.theme.slate"
    label = "slate"
    version = "5.3.2"
    verbose_name = f"Alliance Auth Slate Theme v{version}"

    def ready(self):
        """
        Ready

        :return:
        :rtype:
        """

        pass  # pylint: disable=unnecessary-pass
