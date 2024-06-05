from rest_framework import response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

# Create your views here.

# Get all users
@api_view(['GET'])
def getUsers(request):
    users=User.objects.all()
    serializer=UserSerializer(users, many=True)
    return response(serializer.data)


# Get single user
@api_view(['GET'])
def getUser(request, pk):
    user=User.objects.get(id=pk)
    serializer=UserSerializer(user, many=False)
    return response(serializer.data)


# add user
@api_view(['POST'])
def addUser(request):
    serializer=UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return response(serializer.data)


# Update User
@api_view(["PUT"])
def updateUser(request, pk):
    user=User.objects.get(id=pk)
    serializer=UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return response(serializer.data)


# delete user
@api_view(['DELETE'])
def deleteUser(request, pk):
    user=User.objects.get(id=pk)
    user.delete()

    return response("Item successfully deleted!")