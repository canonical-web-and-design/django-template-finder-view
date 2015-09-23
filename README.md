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
