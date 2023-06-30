from rest_framework.views import APIView
from rest_framework.response import Response

import uuid

class HelloApiView(APIView):
    """Test API View"""
    
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'User HTTP methods get',
            'User HTTP methods post',
            'User HTTP methods patch',
            'User HTTP methods delete'
        ]
        
        return Response({'message': "Hello World", "an_apiview": an_apiview})


class Runbooks(APIView):
    """Test Runbooks API"""
    
    def get(self, request, foramt=None):
        """Returns runbook api response"""
        
        return Response({"message": "server response", "entity": uuid.uuid4()})