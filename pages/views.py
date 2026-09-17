from django.shortcuts import render


# Each view is a function that receives the incoming request and
# returns a response. render() finds the template and sends it back.

def home(request):
    return render(request, "pages/home.html")


def about(request):
    return render(request, "pages/about.html")
