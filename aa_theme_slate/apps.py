"""
App Config
"""

# Django
from django.apps import AppConfig

# AA Theme Slate
from aa_theme_slate import __version__


class AaThemeConfig(AppConfig):
    """
    App config
    """

    name = "aa_theme_slate"
    label = "aa_theme_slate"
    verbose_name = f'Bootstrap Theme "Slate" for Alliance Auth v{__version__}'
