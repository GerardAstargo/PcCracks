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

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_cliente(request, id):

    try:
        cliente = Cliente.objects.get(Rut = id)
    except Cliente.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        seralizer = ClienteSerializers ( cliente, data = data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data)
        else:
            return Response(seralizer.errors,status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cliente.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)