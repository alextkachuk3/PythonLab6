from django.shortcuts import render

from .models import MetroStation


def metro(request):
    stations_list = MetroStation.objects.all()
    return render(request, 'main/metro.html',
                  {'stations_list': stations_list})
