# Alliance Auth Theme: Slate

This is the [Bootstrap theme Slate](https://bootswatch.com/3/slate/) converted into
a theme for Alliance auth.

![AA Theme: Slate](https://raw.githubusercontent.com/ppfeufer/aa-theme-slate/master/aa_theme_slate/images/aa_theme_slate.jpg)

## Installation

```shell
pip install aa-theme-slate
```

Now open your `local.py` and add the following right below your `INSTALLED_APPS`:
```python
# Slate Thame - https://github.com/ppfeufer/aa-theme-slate
INSTALLED_APPS.insert(0, "aa_theme_slate")
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
