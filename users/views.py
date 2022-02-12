from django.conf import settings
import jwt
from rest_framework import generics
from users.serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework.response import Response
from .utils import Util
from rest_framework import status
from rest_framework.views import APIView
# Create your views here
class RegsiterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self,request):
        user =request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #return Response(serializer.data)
        user_data= serializer.data
        user = User.objects.get(email=user_data['email'])
        token= RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        absurl = 'http://'+ current_site + relativeLink + "?token="+str(token)
        email_body = 'Hi' + user.username + 'Use this link to verify Email \n'+ absurl
        data = [{'email_boday': email_body, 'to_email': user.email, 'email_subject': 'verify your email'}]
        Util.send_email(data)
        return Response(user_data , status=status.HTTP_201_CREATED)

class VerifyEmail(APIView):
    def get(self, request):
        token= request.GET.get('token')
        try:
            payload= jwt.decode(token, key = settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified= True
                user.save()
            return Response({'email' : 'Sucessfully activated'}, status= status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as e:
            return Response({'error': 'Activation Link Experied'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError as e:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)