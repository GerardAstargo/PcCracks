from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from pcracks.models import Cliente
from .serializers import ClienteSerializers, EmpleadoSerializers
# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def lista_clientes(request):
    if request.method == 'GET':
        cliente = Cliente.objects.all()
        serializer = ClienteSerializers(cliente,many =True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClienteSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)