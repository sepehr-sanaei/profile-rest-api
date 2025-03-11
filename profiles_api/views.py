from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
# Create your views here.


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of API view features"""
        an_apiview = [
            "hello my name is sepehr",
            "This is an api test",
            "Hello world!",
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """Create a Hello message for out name"""
        serializer = self.serializer_class(data=request.data)


        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({"method":"PUT"})

    def patch(self, request, pk=None):
        """handle a partial update for an object"""
        return Response({"method":"PATCH"})

    def delete(self, request, pk=None):
        """Handle deleting an object"""
        return Response({"method":"DELETE"})
