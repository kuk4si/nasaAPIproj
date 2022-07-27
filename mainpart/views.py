from django.shortcuts import render
from .utils import NasaApi
from .forms import *


def index(request):
    return render(request, 'mainpart/index.html')


def asteroids_neows(request):
    form = AsteroidsNeoWsForm()
    if request.method == "POST":
        form = AsteroidsNeoWsForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            api_obj = NasaApi()
            result = api_obj.get_asteroids_neows(str(start_date))
            context = {'form': form, 'result': result}
            return render(request, 'mainpart/AsteroidsNeoWs.html', context)
    context = {'form': form}
    return render(request, 'mainpart/AsteroidsNeoWs.html', context)


def neo_lookup(request):
    form = NeoLookupForm()
    if request.method == "POST":
        form = NeoLookupForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            api_obj = NasaApi()
            result = api_obj.get_neo_lookup(id)
            if result:
                context = {'form': form, 'result': result}
            else:
                context = {'form': form, 'result': False}
            return render(request, 'mainpart/NeoLookup.html', context)
    context = {'form': form}
    return render(request, 'mainpart/NeoLookup.html', context)


def mars_rover_photos(request):
    """ Та же форма, что для поиска астероидов по дате """
    form = AsteroidsNeoWsForm()
    if request.method == "POST":
        form = AsteroidsNeoWsForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['start_date']
            api_obj = NasaApi()
            result = api_obj.get_mars_rover_photos(str(date))
            context = {'form': form, 'result': result}
            return render(request, 'mainpart/MarsRoverPhotos.html', context)
    context = {'form': form}
    return render(request, 'mainpart/MarsRoverPhotos.html', context)