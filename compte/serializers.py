from rest_framework import serializers
#from monApp.models import client
from django.contrib.auth import authenticate

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = client
        fields = ('id', 'username', 'email', 'telephone')
    

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = client
        fields = ('id', 'username', 'email', 'password', 'telephone')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data) 
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Nom d'utilisateur ou mot de passe incorrecte")
