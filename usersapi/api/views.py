# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import UserDjango
from .serializers import UserDjangoSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import UserDjangoSerializer


# Create your views here.
@csrf_exempt
def usersIndex(request):
    if request.method == 'GET':
        return getUsers()
    elif request.method == 'POST':
        return postUser(request)


def postUser(request):
    data = JSONParser().parse(request)
    serializer = UserDjangoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse('User created', status=201)
    return JsonResponse(serializer.errors, status=400)


def getUsers():
    users = UserDjango.objects.all()
    serializer = UserDjangoSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def getUser(request, id):
    try:
        user = UserDjango.objects.get(pk=id)
    except UserDjango.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserDjangoSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserDjangoSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('User updated', status=200)
        return JsonResponse(serializer.errorr, stauts=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse('User deleted', status=204)