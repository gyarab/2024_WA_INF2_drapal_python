from django.shortcuts import render, get_object_or_404
from content.models import Building, Architect, Style

# Create your views here.

def home(request):
    buildings = Building.objects.order_by('year')
    return render(request, 'content/home.html', {'buildings': buildings})

def building(request, id):
    building = get_object_or_404(Building, pk=id)

    return render(request, 'content/building.html', {'building': building})

def architect(request, id):
    architect = get_object_or_404(Architect, pk=id)

    return render(request, 'content/architect.html', {'architect': architect})

def style(request, id):
    style = get_object_or_404(Style, pk=id)

    return render(request, 'content/style.html', {'style': style})
