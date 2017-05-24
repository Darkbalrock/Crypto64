from django.shortcuts import render

def index(request):
    return render(request, 'Fourier/index.html', {})