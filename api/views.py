from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from api.models import Toy
from api.serializers import ToySerializer

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

# Create your views here.
@api_view(['GET', 'POST'])
def toys_list(request):
    if request.method == 'GET':
        toys = Toy.objects.all()
        toys_serializer = ToySerializer(toys, many=True)
        return JSONResponse(toys_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        toy_data = JSONParser().parse(request)
        toy_serializer = ToySerializer(data=toy_data, many=False)

        if toy_serializer.is_valid():
            toy_serializer.save()
            return JSONResponse(toy_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(toy_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def toys_detail(request, pk):
    try:
        toy = Toy.objects.get(pk=pk)
    except Toy.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        toy_serializer = ToySerializer(toy)
        return JSONResponse(toy_serializer.data)

    elif request.method == 'PUT':
        toy_data = JSONParser().parse(request)
        toy_serializer = ToySerializer(toy, data=toy_data)

        if toy_serializer.is_valid():
            toy_serializer.save()
            return JSONResponse(toy_serializer.data)
        return JSONResponse(toy_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        toy.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)