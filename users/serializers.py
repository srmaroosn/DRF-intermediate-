from rest_framework import serializers
from .models import User
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length= 220, min_length= 8 ,write_only=True)
    class Meta:
        model= User
        fields= ['email' ,'username']
    def validate(self, attrs):
        email= attrs.get('email', '')
        username =attrs.get('username','')

        if username.alnum():
            raise serializers.ValidationError('username must be alphanumeric')
        return attrs

        def create(self.validate_date):
            

