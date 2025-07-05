"""
Helper functions for static integrity calculations
"""

# Standard Library
import os
from pathlib import Path

# Third Party
from sri import Algorithm, calculate_integrity

# Django
from django.conf import settings
from django.templatetags.static import static

# Alliance Auth
from allianceauth.services.hooks import get_extension_logger

# Alliance Auth (External Libs)
from app_utils.logging import LoggerAddTag

# AA Theme Slate
from aa_theme_slate import __title__

logger = LoggerAddTag(my_logger=get_extension_logger(__name__), prefix=__title__)


def calculate_integrity_hash(static_file_path: str) -> str:
    """
    Calculates the integrity hash for a given static file

    :param self:
    :type self:
    :param static_file_path: The file path relative to the `aa_theme_slate/static/aa_theme_slate` folder
    :type static_file_path: str
    :return: The integrity hash
    :rtype: str
    """

    file_path = os.path.join(
        settings.STATIC_ROOT, static_file_path.replace("/static/", "")
    )

    integrity_hash = calculate_integrity(
        path=Path(file_path), algorithm=Algorithm.SHA512
    )

    return integrity_hash


def get_theme_hook_static(static_file: str, script_type: str = None) -> dict:
    """
    Get the static file details for a theme hook

    :param static_file: The file path relative to the `aa_theme_slate/static/aa_theme_slate` folder
    :type static_file: str
    :param script_type: The script type
    :type script_type: str
    :param with_version: Includes the version number in the URL
    :type with_version: bool
    :return: The static file details
    :rtype: dict
    """

    static_file_path = static(static_file)

    return_value = {"url": static_file_path}

    # Calculate integrity hash if not in debug mode
    if not settings.DEBUG:
        integrity = calculate_integrity_hash(static_file_path=static_file_path)
        return_value["integrity"] = integrity

    # Add the script type if provided
    if script_type:
        return_value["js_type"] = script_type

    return return_value
