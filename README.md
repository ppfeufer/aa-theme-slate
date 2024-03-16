# Alliance Auth Theme: Slate<a name="alliance-auth-theme-slate"></a>

[![Version](https://img.shields.io/pypi/v/aa-theme-slate?label=release "Version")](https://pypi.org/project/aa-theme-slate/)
[![License](https://img.shields.io/badge/license-GPLv3-green "License")](https://pypi.org/project/aa-theme-slate/)
[![Python](https://img.shields.io/pypi/pyversions/aa-theme-slate "Python")](https://pypi.org/project/aa-theme-slate/)
[![Django](https://img.shields.io/pypi/djversions/aa-theme-slate?label=django "Django")](https://pypi.org/project/aa-theme-slate/)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ppfeufer/aa-theme-slate/master.svg)](https://results.pre-commit.ci/latest/github/ppfeufer/aa-theme-slate/master)
[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000.svg "Code Style: black")](http://black.readthedocs.io/en/latest/)
[![Automated Checks](https://github.com/ppfeufer/aa-theme-slate/actions/workflows/automated-checks.yml/badge.svg "Automated Checks")](https://github.com/ppfeufer/aa-theme-slate/actions/workflows/automated-checks.yml)
[![codecov](https://codecov.io/gh/ppfeufer/aa-theme-slate/branch/master/graph/badge.svg?token=J9PBF0HM8C "codecov")](https://codecov.io/gh/ppfeufer/aa-theme-slate)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg "Contributor Covenant")](https://github.com/ppfeufer/aa-forum/blob/master/CODE_OF_CONDUCT.md)
[![Discord](https://img.shields.io/discord/790364535294132234?label=discord "Discord")](https://discord.gg/zmh52wnfvM)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/N4N8CL1BY)

This is the [Bootstrap theme Slate](https://bootswatch.com/3/slate/) converted into
a theme for Alliance auth.

______________________________________________________________________

<!-- mdformat-toc start --slug=gitlab --maxlevel=6 --minlevel=1 -->

- [Alliance Auth Theme: Slate](#alliance-auth-theme-slate)
  - [Installation](#installation)

<!-- mdformat-toc end -->

______________________________________________________________________

![AA Theme: Slate](https://raw.githubusercontent.com/ppfeufer/aa-theme-slate/master/aa_theme_slate/images/aa_theme_slate.jpg)

## Installation<a name="installation"></a>

> \[!NOTE\]
>
> **Alliance Auth Theme Slate >= 2.0.0 needs at least Alliance Auth v4.0.0!**
>
> Please make sure to update your Alliance Auth instance _before_ you install this
> module or update to the latest version, otherwise an update to Alliance Auth will
> be pulled in unsupervised.
>
> The last version of Alliance Auth Theme Slate that supports Alliance Auth v3 is `1.7.1`.

```shell
pip install aa-theme-slate
```

Now open your `local.py` and add the following right below your `INSTALLED_APPS`:

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

    # Set Slate Bootstrap Theme for Alliance Auth as the default theme (optional)
    DEFAULT_THEME = "aa_theme_slate.theme.slate.auth_hooks.AaSlateThemeHook"
    DEFAULT_THEME_DARK = "aa_theme_slate.theme.slate.auth_hooks.AaSlateThemeHook"  # Legacy AAv3 user.profile.night_mode=1
```

**Important**

If you are using `AA-GDPR`, the template stuff needs to be **after** the `AA_GDPR`
entry, like this:

```python
# GDPR Compliance
INSTALLED_APPS.insert(0, "aagdpr")
AVOID_CDN = True


# Slate Thame - https://github.com/ppfeufer/aa-theme-slate
INSTALLED_APPS.insert(0, "aa_theme_slate")
```
