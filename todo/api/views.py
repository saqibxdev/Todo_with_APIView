from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response        
from api.serializers import UserSerializer
from rest_framework import status
from django.http import Http404
class UserList(APIView):
    def get(self,request,*args,**kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get_object(self,user_id):
        try:
            return User.objects.get(pk = user_id)   
        except Snippet.DoesNotExist:
            raise Http404

    def get(self,request,user_id,*args,**kwargs):
        user = self.get_object(user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self,request,user_id,*args,**kwargs):
        user = self.get_object(user_id)
        serializer = UserSerializer(instance = user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,user_id,*args,**kwargs):
        user = self.get_object(user_id)
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)