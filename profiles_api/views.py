from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


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