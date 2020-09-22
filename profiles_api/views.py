from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets


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