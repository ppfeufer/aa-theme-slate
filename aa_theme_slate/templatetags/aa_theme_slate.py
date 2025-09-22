"""
Template filter for AA Theme Slate templates
"""

# Django
from django.template.defaulttags import register


@register.filter
def startswith(haystack, needle):
    """
    Custom Django template filter to check if a string starts with a specified substring.

    This filter can be used in Django templates to evaluate whether the given string
    starts with the provided substring. If the condition is met,
    it returns `True`; otherwise, `False`.

    Usage:
        {% load aa_theme_slate %}

        {% if string|starts_with:"substring" %}
            <!-- Render content if the string starts with the substring -->
        {% endif %}

    :param haystack: The string to be checked.
    :type haystack: str
    :param needle: The substring to check for at the start of `haystack`.
    :type needle: str
    :return: `True` if `haystack` starts with `needle`, otherwise `False`.
    :rtype: bool
    """

    return haystack.startswith(needle)
