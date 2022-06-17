from django.http import JsonResponse
from .models import Editier2api
from .serializers import Editier2apiSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET", "POST"])
def testdata(request, format=None):
    # get all the tickets
    # serialize them
    # return json
    # be careful with the syntax error, extra()
    if request.method == "GET":
        all_data = Editier2api.objects.all()
        serializer = Editier2apiSerializer(all_data, many=True)
        return JsonResponse({"testdata": serializer.data}, safe=False)

    if request.method == "POST":
        serializer = Editier2apiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def individual_data(request, id, format=None):
    # create an var to hold the object, return not found if id doesnt match
    try:
        each_data = Editier2api.objects.get(pk=id)
    except Editier2api.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        ##variable name spelled wrong
        serializer = Editier2apiSerializer(each_data)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = Editier2apiSerializer(each_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        each_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
