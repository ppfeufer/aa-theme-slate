"""
Auth hooks for Terra Nanotech theme
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
    Terra Nanotech Corp Auth Theme
    https://github.com/terra-nanotech/tn-nt-auth-templates/
    """

    def __init__(self):
        """
        Init
        """

        ThemeHook.__init__(
            self,
            "Slate",
            "Bootstrap Slate Theme",
            css=[
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        "aa_theme_slate/theme/aav4/bootstrap/v5.3.2/css/bootstrap.min.css",
                    ),
                    "integrity": "sha512-1y2MKGMn41OgOgazBAujc8GPUCUDUoS4+3nPlH7mLDmgzIpcLsrAj0m/01xhpGbqbSWiqrnNUxkM/RhugT7ZIA==",
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
                        "aa_theme_slate/theme/aav4/bootstrap/v5.3.2/javascript/bootstrap.min.js",
                    ),
                    "integrity": "sha512-BPNIL/15RLxikcVNXWuFX/0zOtsuNphZCXgIL9im3QZ8ZB3oyGgbokg2pC757WCbpDRLxFnf89pdm6KHO8fehA==",
                },
            ],
            header_padding="3.6em",
        )


@hooks.register("theme_hook")
def register_aa_slate_hook():
    """
    Registers the Terra Nanotech theme hook

    :return:
    :rtype:
    """

    return AaSlateThemeHook()
