from rest_framework import serializers
from users.utils import Util
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.utils.encoding import smart_str, force_str,smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length= 220, min_length=6 ,write_only=True)

    class Meta:
        model= User
        fields= ['email' ,'username','password']
    def validate(self, attrs):
        email= attrs.get('email', '')
        username =attrs.get('username','')

        if username.isalnum():
            raise serializers.ValidationError('username must be alphanumeric')
        return attrs

    def create(self,validated_date):
            return User.objects.create_user(**validated_date)
            
class EmailVerificationSerializer(serializers.ModelSerializer):
    token =serializers.CharField(max_length= 555)
    class Meta:
        model= User
        fields = ['tokens']

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length= 220)
    password = serializers.CharField(max_length=220, write_only= True)
    username = serializers.CharField(max_length=220, read_only= True)
    tokens = serializers.CharField(max_length=220, read_only= True)

    class Meta:
        model= User
        fields= ['email' ,'password','username','tokens']
    def validate(self, attrs):
        email= attrs.get('email', '')
        password =attrs.get('password','')
        user = auth.authenticate(email=email, password=password )
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disable , contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email not verified')

        return{
            'email':user.email,
            'username': user.username,
            'tokens': user.tokens
        }
class RestPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)
    class Meta:
        fields= ['email']
    def vaildate(self, attrs):
        email= attrs[data].get('email','')
        if User.objects.filter(email=email).exits():
            user = User.objects.get(email= email)
            uidb64 = urlsafe_base64_encode(user.id)
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request=attrs['data'].get('request')).domain
            relative_link = reverse('password-reset-confirm', kwargs={'uidb64':uidb64, 'token':token})
            absurl = 'http://'+current_site + relative_link
            email_body= 'hello \n Use this link to reset your password'+ absurl
            data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Reset your password'}
            Util.send_email(data)
        return super().validate(attrs)



