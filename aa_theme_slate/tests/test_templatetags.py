"""
Unit tests for AA Theme Slate template tags.

This module contains unit tests for custom template tags used in the AA Theme Slate.
The tests ensure that the template tags behave as expected under various conditions.
"""

# Django
from django.template import Context, Template
from django.test import TestCase


class TestTemplateTags(TestCase):
    """
    Unit test class for verifying the functionality of AA Theme Slate template tags.

    This class contains test cases to ensure that the custom template tags
    used in the AA Theme Slate behave as expected under various conditions.
    """

    def setUp(self):
        """
        Sets up the test context for the test cases.

        This method initializes a Django template context with a predefined
        content string. The context is used in the template rendering tests
        to verify the behavior of custom template tags.

        :return:
        :rtype:
        """

        self.context = Context(
            {"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."}
        )

    def test_should_return_content_when_string_starts_with_substring(self):
        """
        Tests that the template renders the content when the string starts with the specified substring.

        This test verifies that the custom `startswith` filter correctly identifies
        when the `content` string begins with the substring "Lorem" and ensures
        that the content is included in the rendered template.

        :return: None
        """

        template_to_render = Template(
            "{% load aa_theme_slate %}"
            '{% if content|startswith:"Lorem" %}{{ content }}{% endif %}'
        )
        rendered_template = template_to_render.render(self.context)

        self.assertInHTML(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            rendered_template,
        )

    def test_should_not_return_content_when_string_does_not_start_with_substring(self):
        """
        Tests that the template does not render the content when the string does not start with the specified substring.

        This test verifies that the custom `startswith` filter correctly identifies
        when the `content` string does not begin with the substring "ipsum" and ensures
        that the content is excluded from the rendered template.

        :return: None
        """

        template_to_render = Template(
            "{% load aa_theme_slate %}"
            '{% if content|startswith:"ipsum" %}{{ content }}{% endif %}'
        )
        rendered_template = template_to_render.render(self.context)

        self.assertNotIn(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            rendered_template,
        )
