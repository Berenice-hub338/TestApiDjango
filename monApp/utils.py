import json
from .models import *

def cartData(request):
	if request.user.is_authenticated:
		client = request.user.client
		commande, created = Commande.objects.get_or_create(client=client, complet=False)
		items = commande.orderitem_set.all()
		cartItems = commande.get_cart_items
	else:
		pass

	return {'cartItems':cartItems ,'order':commande, 'items':items}