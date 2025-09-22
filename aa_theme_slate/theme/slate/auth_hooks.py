"""
Auth hooks for Slate Bootstrap Theme for Alliance Auth
"""

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
            self=self,
            name="Slate",
            description="Slate Bootstrap Theme for Alliance Auth",
            html_tags={"data-theme": "slate"},
            css=[],
            css_template="aa_theme_slate/assets/css.html",
            js=[],
            js_template="aa_theme_slate/assets/js.html",
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
