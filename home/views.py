from django.shortcuts import render


# Home/index page view
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
