from ctypes import windll

from django.shortcuts import render

# Create your views here.
def index(request):
    temp = 38.7
    humidity = 12
    wind = 15
    city = 'zanzibar'
    is_sunny = True
    user = ["Jane", "Joseph","moha"]
# package
    data = {
        'temperature': temp,
        'humidity': humidity,
        'wind': wind,
        'city': city,
        'is_sunny': is_sunny,
        'user': user
    }
    return render(request,'home.html',data)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')
