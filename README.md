**NB:**

This project has been superseded by [canonicalwebteam.django-views](https://github.com/canonical-webteam/django-views), which contained an equivalent [TemplateFinder view class](https://github.com/canonical-webteam/django-views/blob/master/canonicalwebteam/django_views/__init__.py#L130). Projects shouldb upgrade to using that package instead.

This project will now be archived.

---

Django template finder view
===

`TemplateFinder` is an extension of `TemplateView` which attempts to load the corresponding templates directly from URLs, without the need to write a view for each URL.

Matching example
---

When Fenchurch parses a URL, it will look for templates in two corresponding locations, e.g.:

    http://example.com/parent/location/ => TEMPLATE_DIR/parent/location.html

Or:

    http://example.com/parent/location/ => TEMPLATE_DIR/parent/location/index.html

Installation
---

```
pip install django-template-finder-view
```

Usage
---

Simply include `TemplateFinder` in a URL match in your `urls.py` file, passing through the `template` argument:

``` python
# [app]/urls.py

from django_template_finder_view import TemplateFinder

...

urlpatterns = [
    ...
    url(r'^(?P<template>.*)$', TemplateFinder.as_view()),
]
```

Configuration
---

`TemplateFinder` will use the default Django template loader to search for templates with the expected names, so the simplest way to configure the templates location is to use the default `TEMPLATE_DIRS` setting, e.g.:

``` python
# [app]/settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    }
]
```

A custom folder to load the templates can be specified. This allows you to keep the URL acessible templates separately from template includes.

``` python
# As a subfolder in templates. Only searching inside `templates/pages/`
TEMPLATE_FINDER_PATH = 'pages'
```

To specify an absolute directory outside templates, it must be added to the `DIRS` setting in `TEMPLATES`.
``` python
# Outside the templates folder
TEMPLATE_FINDER_PATH = os.path.join(BASE_DIR, 'pages')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            TEMPLATE_FINDER_PATH,
        ],
    }
]
```
