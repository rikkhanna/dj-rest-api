from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from profiles_api import serializers, models
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import permissions


class HelloApi(APIView):

    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """ returns a list of APIView features """

        an_api = [
            'API','Django','REST'
        ]

        return Response({'message':'Hello!','an_api':an_api})

    
    def post(self,request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update an object"""
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk=None):
        """Handle deleting an object"""
        return Response({'method':'DELETE'})


class HelloViewSets(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self,request):

        a_view = [ 'some text', 'some more text']
        
        return Response({'message':'list','a_view':a_view})
    

    def create(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """updating an object by its ID"""
        return Response({'http_method':'PUT'})  
    
    def partial_update(self, request, pk=None):
        """partially updating an object by its ID"""
        return Response({'http_method':'PATCH'})

    def delete(self, request, pk=None):
        """deleting an object by its ID"""
        return Response({'http_method':'DELETE'})


class UserProfileModelViewSet(viewsets.ModelViewSet):
    """Simple viewset for handling user profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateUserOWnProfile,)
    filter_backends =   (filters.SearchFilter,)
    search_fields = ('name','email',)

class UserLoginAPIView(ObtainAuthToken):
    """Handle creating user authentication token"""

    #ObtainAuthToken does not enable itself in browser
    renderer_classes    =   api_settings.DEFAULT_RENDERER_CLASSES
    #it adds the renderer classes to obtainAuthToken view which will enable in django admin


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes  =   (TokenAuthentication,)
    serializer_class        =   serializers.ProfileFeedItemSerializer
    queryset                =   models.ProfileFeedItem.objects.all()

    def performed_create(self, serializer):
        """Sets the user profile to logged in user"""
        #To customize the logic for creating an object
        #This function will gets called with every HTTP POST request to ViewSet

        #This save function is used to save the contents of the serializer
        # to an object in the database
        serializer.save(user_profile=self.request.user)
        #request object gets passed into all view sets every time a request is made
        #It contains all of the details about the requestbeing made to the ViewSet
        
        

