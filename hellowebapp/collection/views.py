from django.shortcuts import render
from .models import Thing
# Create your views here.
def index(request): 
    # this is your new view
    things = Thing.objects.all()
    number = 1
    return render(request, 'index.html', {
        'things': things,
        })

def thing_detail(request, slug): 
    # this is your new view
    things = Thing.objects.get(slug=slug)
    number = 1
    return render(request, 'things/things_detail.html', {
        'thing': things,
        })