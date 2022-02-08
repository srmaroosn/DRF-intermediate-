from django.shortcuts import render
from rest_framework import generics
from users.serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework.response import Response
# Create your views here
class RegsiterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self,request):
        user =request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        #user_data= serializer.data
        #user = User.objects.get(email=user_data['email'])
        #token= RefreshToken.for_user(user).access_token
        #current_site = get_current_site(request).domain
        #relativeLink = reverse

