from django.apps import AppConfig

from . import __version__


class AaThemeConfig(AppConfig):
    name = "aa_theme_slate"
    label = "aa_theme_slate"
    verbose_name = 'Bootstrap Theme "Slate" for Alliance Auth v{version}'.format(
        version=__version__
    )
