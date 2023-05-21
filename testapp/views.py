from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from .serializers import NameSerializer


class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        colors = ['red', 'green', 'yellow', 'blue']
        return Response({'msg': 'Happly new year', 'colours': colors})
    def post(self, request, *args, **kwargs):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = "Hello {}".format(name)
            return Response({'msg': msg})
        else:
            return Response(serializer.errors, status=400)
    def put(self, request, *args, **kwargs):
        return Response({'msg': 'This msg from put method'})
    def patch(self, request, *args, **kwargs):
        return Response({'msg': 'This msg from patch method'})
    def delete(self, request, *args, **kwargs):
        return Response({'msg': 'This msg from delete method'})


class TestViewSet(ViewSet):
    def list(self, request):
        colors = ['red', 'green', 'yellow', 'blue']
        return Response({'msg': 'Happly new year', 'colours': colors})
    def create(self, request):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = "Hello {}".format(name)
            return Response({'msg': msg})
        else:
            return Response(serializer.errors, status=400)
    def retrieve(self, request, pk=None):
        return Response({'msg': 'This msg from retrieve method'})
    def update(self, request, pk=None):
        return Response({'msg': 'This msg from update method'})
    def partial_update(self, request, pk=None):
        return Response({'msg': 'This msg from partial_update method'})
    def destroy(self, request, pk=None):
        return Response({'msg': 'This msg from destroy method'})
