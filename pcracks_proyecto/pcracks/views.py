from django.shortcuts import render

# Create your views here.
def menu_off (request):
        nombre="Nicolas"

    contexto={
        "nomb": nombre
    }
    return render(request, 'pcracks/menuOFF.html',contexto)

def login (request):
    return render (request, 'pcracks/Login.html')
