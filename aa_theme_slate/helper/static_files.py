"""
Helper functions for static integrity calculations
"""

# Standard Library
import os
from pathlib import Path
from urllib.parse import urljoin

# Third Party
from sri import Algorithm, calculate_integrity

# Django
from django.conf import settings

# Alliance Auth
from allianceauth.services.hooks import get_extension_logger

# Alliance Auth (External Libs)
from app_utils.logging import LoggerAddTag

# AA Theme Slate
from aa_theme_slate import __title__, __version__
from aa_theme_slate.constants import SLATE_STATIC_DIR

logger = LoggerAddTag(my_logger=get_extension_logger(__name__), prefix=__title__)


def calculate_integrity_hash(relative_file_path: str) -> str:
    """
    Calculates the integrity hash for a given static file

    :param self:
    :type self:
    :param relative_file_path: The file path relative to the `aa_theme_slate/static/aa_theme_slate` folder
    :type relative_file_path: str
    :return: The integrity hash
    :rtype: str
    """

    file_path = os.path.join(SLATE_STATIC_DIR, relative_file_path)
    integrity_hash = calculate_integrity(
        path=Path(file_path), algorithm=Algorithm.SHA512
    )

    return integrity_hash


def get_theme_hook_static(
    static_file: str, script_type: str = None, with_version: bool = False
) -> dict:
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

    return_value = {
        "url": urljoin(
            base=settings.STATIC_URL,
            url=f"aa_theme_slate/{static_file}",
        ),
    }

    # Calculate integrity hash if not in debug mode
    if not settings.DEBUG:
        integrity = calculate_integrity_hash(relative_file_path=static_file)
        return_value["integrity"] = integrity

    # Add the script type if provided
    if script_type:
        return_value["js_type"] = script_type

    # Add the version number if requested
    if with_version:
        return_value["url"] += f"?v={__version__}"

    return return_value
