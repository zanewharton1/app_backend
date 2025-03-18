from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import LoginCredentials
from .serializers import CredentialsSerializer

@api_view(['GET', 'POST'])
def credentials_handler(request):

    if request.method == 'GET':
        credentails = LoginCredentials.objects.all()

        serializer = CredentialsSerializer(credentails, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CredentialsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def credentials_details(request, id):
    credentials = LoginCredentials.objects.get(pk=id)

    if request.method == 'GET':
        serializer = CredentialsSerializer(credentials)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CredentialsSerializer(credentials, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        credentials.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
    