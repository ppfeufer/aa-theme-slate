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
    verbose_name = 'Bootstrap Theme "Slate" for Alliance Auth v{version}'.format(
        version=__version__
    )
