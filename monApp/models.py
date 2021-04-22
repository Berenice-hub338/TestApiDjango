from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class Produit(models.Model):
	nom = models.CharField(max_length=200)
	prix = models.FloatField()
	image = models.ImageField(null=True, blank=True, upload_to='images/')

	def __str__(self):
		return self.nom


class Commande(models.Model):
	client = models.ForeignKey(User, on_delete=models.CASCADE)
	date_commande = models.DateTimeField(auto_now_add=True)
	complet = models.BooleanField(default=False)

	def __str__(self):
		return str(self.id)

	
class ProduitCommande(models.Model):
	client = models.ForeignKey(User, on_delete=models.CASCADE)
	produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
	commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
	quantite = models.IntegerField(default=0)
	date_ajout = models.DateTimeField(auto_now_add=True)

	def prix_total(self):
		total = self.produit.prix * self.quantite
		return total