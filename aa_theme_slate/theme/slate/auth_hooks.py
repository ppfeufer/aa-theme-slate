"""
Auth hooks for Slate Bootstrap Theme for Alliance Auth
"""

# Standard Library
from urllib.parse import urljoin

# Django
from django.conf import settings

# Alliance Auth
from allianceauth import hooks
from allianceauth.theme.hooks import ThemeHook


class AaSlateThemeHook(ThemeHook):
    """
    Slate Bootstrap Theme for Alliance Auth
    https://github.com/ppfeufer/aa-theme-slate
    """

    def __init__(self):
        """
        Init
        """

        ThemeHook.__init__(
            self,
            "Slate",
            "Slate Bootstrap Theme for Alliance Auth",
            css=[
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        "aa_theme_slate/theme/aav4/bootstrap/v5.3.3/css/bootstrap.min.css",
                    ),
                    "integrity": "sha512-lF+xS8uroqRohnQyVXSTrsB+YgYcwHKVm8T6atFzc/cnOW1RTnc6x00585jS74sz9GPrNbzH4QkP8JICSXNP0Q==",
                },
            ],
            js=[
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        "aa_theme_slate/theme/aav4/popper/v2.11.8/popper.min.js",
                    ),
                    "integrity": "sha512-fhcY1KxngNJ4jVhZBdmrLv4/NH31jrNM45fpxytokYp06cd7Ug05E3gximUQmukhES9Xf0kbV5F1nHVqWq2bvQ==",
                },
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        "aa_theme_slate/theme/aav4/bootstrap/v5.3.3/javascript/bootstrap.min.js",
                    ),
                    "integrity": "sha512-gNyiMtmOs5iIO2fjMFZRSR1s9Espoi+fdDtNuSh1iMpeRminsho2AA7767qpfkYqskd9PtUfMwAg0KdKJsMTuQ==",
                },
            ],
            header_padding="3.6em",
        )


@hooks.register("theme_hook")
def register_aa_slate_hook():
    """
    Registers the Slate Bootstrap Theme for Alliance Auth hook

    :return:
    :rtype:
    """

    return AaSlateThemeHook()
