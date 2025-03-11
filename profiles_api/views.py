from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of API view features"""
        an_apiview = [
            "hello my name is sepehr",
            "This is an api test",
            "Hello world!",
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
