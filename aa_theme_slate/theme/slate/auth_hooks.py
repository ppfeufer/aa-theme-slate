"""
Auth hooks for Slate Bootstrap Theme for Alliance Auth
"""

# Alliance Auth
from allianceauth import hooks
from allianceauth.theme.hooks import ThemeHook

# AA Theme Slate
from aa_theme_slate.helper.static_files import get_theme_hook_static


class AaSlateThemeHook(ThemeHook):
    """
    Slate Bootstrap Theme for Alliance Auth
    https://github.com/ppfeufer/aa-theme-slate
    """

    def __init__(self):
        """
        Init
        """

        css_static_files = [
            get_theme_hook_static(
                static_file="aa_theme_slate/theme/aav4/libs/bootswatch/v5.3.3/slate/css/bootstrap.min.css"
            ),
            get_theme_hook_static(
                static_file="aa_theme_slate/theme/aav4/css/community-apps.min.css"
            ),
        ]

        js_static_files = [
            get_theme_hook_static(
                static_file="aa_theme_slate/theme/aav4/libs/popper/v2.11.8/popper.min.js"
            ),
            get_theme_hook_static(
                static_file="aa_theme_slate/theme/aav4/libs/bootswatch/v5.3.3/slate/javascript/bootstrap.min.js"
            ),
        ]

        ThemeHook.__init__(
            self=self,
            name="Slate",
            description="Slate Bootstrap Theme for Alliance Auth",
            html_tags={"data-theme": "slate"},
            css=css_static_files,
            js=js_static_files,
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
