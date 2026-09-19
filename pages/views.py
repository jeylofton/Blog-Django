from django.views.generic import TemplateView


# Each view is a function that receives the incoming request and
# returns a response. render() finds the template and sends it back.

class HomePageView(TemplateView):
    template_name = "pagesTemplates/home.html"

class AboutPageView(TemplateView):
    template_name = "pagesTemplates/about.html"