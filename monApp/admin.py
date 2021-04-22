from django.contrib import admin

from .models import Produit, Commande,  ProduitCommande

admin.site.register(Produit)
admin.site.register(Commande)
admin.site.register(ProduitCommande)
