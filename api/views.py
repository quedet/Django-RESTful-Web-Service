from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from api.models import Toy
from api.serializers import ToySerializer

# Create your views here.
@api_view(['GET', 'POST'])
def toys_list(request):
    if request.method == 'GET':
        toys = Toy.objects.all()
        toys_serializer = ToySerializer(toys, many=True)
        return Response(toys_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        toy_data = request.data
        toy_serializer = ToySerializer(data=toy_data, many=False)

        if toy_serializer.is_valid():
            toy_serializer.save()
            return Response(toy_serializer.data, status=status.HTTP_201_CREATED)
        return Response(toy_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def toys_detail(request, pk):
    toy = get_object_or_404(Toy, pk=pk)

    if request.method == 'GET':
        toy_serializer = ToySerializer(toy)
        return Response(toy_serializer.data)

    elif request.method == 'PUT':
        toy_data = request.data
        toy_serializer = ToySerializer(toy, data=toy_data)

        if toy_serializer.is_valid():
            toy_serializer.save()
            return Response(toy_serializer.data)
        return Response(toy_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        toy.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)