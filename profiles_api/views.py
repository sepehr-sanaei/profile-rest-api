from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions
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

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'my name is qasem',
            'I have a pride',
            'my pride is better then buggati shiron'
        ]

        return Response({'message':'Hello!', 'a_viewset':a_viewset})


    def create(self, request):
        """Create a new Hello message for name"""
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

    def retrieve(self, request, pk=None):
        """Get an object by its pk"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handles Updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handles partial object on an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handles Removing an object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating user profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfille,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
