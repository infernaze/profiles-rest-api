from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control ove your application logic',
            'Is maped manually to URLs',
            'Yay, RESTfull ends baby.'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
