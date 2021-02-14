from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status


class HelloAPIView(APIView):
    """Test APIView"""

    def get(self,request,format=None):
        features = [
            'Great features to share',
            'exelents results',
            'very fast comunications'
        ]

        return Response({'message':'hello', 'features':features})


    def post(self,request,format=None):
        return Response({'message':'You sent a post method'})


class HelloViewSet(ViewSet):
    """Test API ViewSet"""

    def list(self,request):
        """Return a hello message"""

        a_viewset = [
            'Powerful feature',
            'minumum effort to code'
            'simple to implement'
        ]

        return Response({'message':'Hello', 'a_viewset':a_viewset})

    def create(self, request):
        return Response({'method':'POST'})

    def retrieve(self, request, pk=None):
        return Response({'method':'GET'})

    def update(self, request, pk=None):
        return Response({'method':'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'method':'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'method':'DELETE'})