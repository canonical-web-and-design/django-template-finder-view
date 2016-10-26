# System
from os.path import join

# Modules
from django.template import loader, TemplateDoesNotExist
from django.views.generic.base import TemplateView
from django.http import Http404
from django.conf import settings


class TemplateFinder(TemplateView):
    """
    A TemplateView that guesses the template name based on the
    url path or redirects if defined in redirects.txt.
    """

    def return_template(self, template_path):
        """
        From a path, return a template file
        <path>/index.html if the path is a directory
        or <path>.html
        """

        template_path = template_path.rstrip('/')

        template_root = getattr(settings, 'TEMPLATE_FINDER_PATH', None)
        if template_root:
            template_path = join(template_root, template_path)

        index = join(template_path, 'index.html')
        template = join(template_path + '.html')
        if self.__template_exists__(template):
            return template
        elif self.__template_exists__(index):
            return index

    def dispatch(self, request, *args, **kwargs):
        """
        This is called when TemplateFinder is run as a view

        It tries to find the template for the request path
        and then passes that template name to TemplateView to render
        """

        clean_path = request.path.strip('/')
        self.template_name = self.return_template(clean_path)

        if self.template_name:
            return super(TemplateFinder, self).dispatch(
                request, *args, **kwargs
            )
        else:
            raise Http404("Can't find page for: %s" % clean_path)

    def __template_exists__(self, path):
        """
        Check if a template exists
        without raising an exception
        """

        try:
            loader.get_template(path)
            return True
        except TemplateDoesNotExist:
            return False
