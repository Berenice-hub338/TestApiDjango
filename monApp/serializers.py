from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['id', 'username', "email", "telephone"]



class CommandeSerializer(serializers.ModelSerializer):
    client = UserSerializer()
    class Meta:
        model= models.Commande
        fields= '__all__'

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Produit
        fields= '__all__'

class ProduitCommandeSerializer(serializers.ModelSerializer):
    client = UserSerializer()
    class Meta:
        model= models.ProduitCommande
        fields= '__all__'