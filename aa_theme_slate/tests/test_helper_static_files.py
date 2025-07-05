"""
Test cases for the the static_files helper module.
"""

# Standard Library
from unittest.mock import patch

# Django
from django.test import TestCase

# AA Theme Slate
from aa_theme_slate.helper.static_files import get_theme_hook_static


class TestGetThemeHookStatic(TestCase):
    """
    Test cases for the get_theme_hook_static function in the static_files helper module.
    """

    def test_returns_static_file_details_with_integrity_in_production(self):
        """
        Test that the function returns static file details with integrity hash in production mode.

        :return:
        :rtype:
        """

        with (
            patch("aa_theme_slate.helper.static_files.settings.DEBUG", False),
            patch(
                "aa_theme_slate.helper.static_files.calculate_integrity_hash",
                return_value="mocked_hash",
            ),
            patch(
                "aa_theme_slate.helper.static_files.static",
                return_value="/static/js/script.js",
            ),
        ):
            result = get_theme_hook_static("js/script.js")

            self.assertEqual(result["url"], "/static/js/script.js")
            self.assertEqual(result["integrity"], "mocked_hash")
            self.assertNotIn("js_type", result)

    def test_returns_static_file_details_without_integrity_in_debug_mode(self):
        """
        Test that the function returns static file details without integrity hash in debug mode.

        :return:
        :rtype:
        """

        with patch("aa_theme_slate.helper.static_files.settings.DEBUG", True):
            result = get_theme_hook_static("css/style.css")

            self.assertEqual(result["url"], "/static/css/style.css")
            self.assertNotIn("integrity", result)
            self.assertNotIn("js_type", result)

    def test_includes_script_type_when_provided(self):
        """
        Test that the function includes the script type when provided.

        :return:
        :rtype:
        """

        with patch("aa_theme_slate.helper.static_files.settings.DEBUG", True):
            result = get_theme_hook_static("js/script.js", script_type="module")

            self.assertEqual(result["url"], "/static/js/script.js")
            self.assertEqual(result["js_type"], "module")
            self.assertNotIn("integrity", result)

    def test_handles_empty_static_file_path(self):
        """
        Test that the function handles an empty static file path correctly.

        :return:
        :rtype:
        """

        with patch("aa_theme_slate.helper.static_files.settings.DEBUG", True):
            result = get_theme_hook_static("")

            self.assertEqual(result["url"], "/static/")
            self.assertNotIn("integrity", result)
            self.assertNotIn("js_type", result)
