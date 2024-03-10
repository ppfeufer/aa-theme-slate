# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

<!--
GitHub MD Syntax:
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

Highlighting:
https://docs.github.com/assets/cb-41128/mw-1440/images/help/writing/alerts-rendered.webp

> [!NOTE]
> Highlights information that users should take into account, even when skimming.

> [!IMPORTANT]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.
-->

## \[In Development\] - Unreleased

<!--
Section Order:

### Added
### Fixed
### Changed
### Deprecated
### Removed
### Security
-->

## \[2.0.0-beta.1\] - 2024-03-10

> \[!NOTE\]
>
> **This version needs at least Alliance Auth v4.0.0b2!**
>
> Please make sure to update your Alliance Auth instance **before**
> you install this version, otherwise, an update to Alliance Auth will
> be pulled in unsupervised.

> \[!IMPORTANT\]
>
> Configuration change!
>
> See the [Update Information](#update-information-for-aav4) section for the new configuration

### Added

- Compatibility with Alliance Auth 4.0.0

### Removed

- Compatibility with Alliance Auth 3

### Update Information for AAv4

The configuration for the theme has changed. You need to update your `local.py`:

```python
# Slate Theme - https://github.com/ppfeufer/aa-theme-slate
INSTALLED_APPS.insert(0, "aa_theme_slate")

if "aa_theme_slate" in INSTALLED_APPS:
    # Remove all other themes
    # If you want to use Slate as the only theme, you need to remove all other themes.
    # INSTALLED_APPS.remove("allianceauth.theme.darkly")
    # INSTALLED_APPS.remove("allianceauth.theme.flatly")
    # INSTALLED_APPS.remove("allianceauth.theme.materia")

    # If you are using AA-GDPR, you need to remove the Darkly, Flatly and Materia themes
    # added by AA-GDPR as well.
    # if "aagdpr" in INSTALLED_APPS:
    #     INSTALLED_APPS.remove("aagdpr.theme.darkly")
    #     INSTALLED_APPS.remove("aagdpr.theme.flatly")
    #     INSTALLED_APPS.remove("aagdpr.theme.materia")

    INSTALLED_APPS += [
        "aa_theme_slate.theme.slate",
    ]

    # Load Slate Bootstrap Theme for Alliance Auth
    DEFAULT_THEME = "aa_theme_slate.theme.slate.auth_hooks.AaSlateThemeHook"
    DEFAULT_THEME_DARK = "aa_theme_slate.theme.slate.auth_hooks.AaSlateThemeHook"  # Legacy AAv3 user.profile.night_mode=1
```

## \[1.7.1\] - 2023-09-18

### Fixed

- Moved Bootstrap icon font to the right directory

## \[1.7.0\] - 2023-09-02

### Changed

- Moved the build process to PEP 621 / pyproject.toml
- Base template for AA 3.6.1 public views
- Minimum requirements
  - Alliance Auth >= 3.6.1

## \[1.6.0\] - 2022-08-05

### Added

- SVG icons for `aa-forum` v1.12.0

### Changed

- Minimum requirements
  - Alliance Auth >= 2.15.1
  - Python >= 3.8

## \[1.5.0\] - 2022-08-05

### Changed

- Updates for AA3

## \[1.4.0\] - 2022-03-02

### Added

- Tests for Python 3.11
- Test suite for AA 3.x and Django 4

### Changed

- Switched to `setup.cfg` as config file, since `setup.py` is deprecated now
- Minimum requirements
  - Alliance Auth >= 2.11.0

### Removed

- Deprecated settings

## \[1.3.0\] - 2021-11-30

### Changed

- Minimum requirements
  - Python >= 3.7
  - Alliance Auth >= 2.9.3

## \[1.2.3\] - 2021-11-20

### Fixed

- Django version in `setup.py`

## \[1.2.2\] - 2021-11-20

### Fixed

- Author in `setup.py`

## \[1.2.1\] - 2021-10-21

### Changed

- Use SITE_NAME as page title

## \[1.2.0\] - 2021-10-17

### Changed

- Compatibility for Alliance Auth 2.9.0

## \[1.1.0\] - 2021-04-19

### Removed

- CSS for dark and light mode, we don't have that with this theme

## \[1.0.1\] - 2021-04-18

### Fixed

- Some typos

## \[1.0.0\] - 2021-04-18

### Added

- initial release
