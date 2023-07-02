from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from profiles_api.models import Destination

import uuid

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'User HTTP methods get',
            'User HTTP methods post',
            'User HTTP methods patch',
            'User HTTP methods delete'
        ]
        
        return Response({'message': "Hello World", "an_apiview": an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        serializer.validate(request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            mobileno = serializer.validated_data.get('mobileno')
            
            try:
                dest = Destination.objects.get(name=name)
            except Exception:
                Destination.objects.create(name=name, mobileno=mobileno)
        
            dest = Destination.objects.get(name=name)
            dest_data = self.serializer_class(dest)
            message = f'Hello {dest_data.data}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Runbooks(APIView):
    """Test Runbooks API"""
    
    def get(self, request, foramt=None):
        """Returns runbook api response"""
        
        return Response({"message": "server response", "entity": uuid.uuid4()})