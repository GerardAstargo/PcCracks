from django.shortcuts import render

# Create your views here.
def menu_off (request):
    return render(request, 'pcracks/menuOFF.html')

def login (request):
    return render (request, 'pcracks/Login.html')
