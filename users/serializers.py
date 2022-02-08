from rest_framework import serializers
from .models import User
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length= 220, min_length= 8 ,write_only=True)
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
            

