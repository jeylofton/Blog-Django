from django.views.generic import TemplateView
from django.shortcuts import HttpResponse, render


# Each view is a function that receives the incoming request and
# returns a response. render() finds the template and sends it back.

class HomePageView(TemplateView):
    template_name = "pagesTemplates/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Jey"
        print(context)
        return context

class AboutPageView(TemplateView):
    template_name = "pagesTemplates/about.html"

def contact_page(request):
    # print(request.__dict__)
    # return HttpResponse("Hello World from a FBV")

    contact_info ={
        "name": "Jey Lofton",
        "address": "Somewhere 125 PAN",
        "email": "loftonjey9@mail.com"
    }

    return render(request, "pagesTemplates/contact.html", contact_info)