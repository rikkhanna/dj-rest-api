from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApi(APIView):

    def get(self, request, format=None):
        """ returns a list of APIView features """
        
        an_api = [
            'API','Django','REST'
        ]

        return Response({'message':'Hello!','an_api':an_api})
