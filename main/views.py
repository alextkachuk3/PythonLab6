from django.shortcuts import render


# Create your views here.

def metro(request):
    return render(request, 'main/metro.html')
