from rest_framework import generics
from rest_framework import permissions
from . import serializers, models



class ProduitListView(generics.ListAPIView):
	queryset = models.Produit.objects.all()
	serializer_class = serializers.ProduitSerializer


class DetailProduitView(generics.RetrieveAPIView):
	queryset = models.Produit.objects.all()
	serializer_class = serializers.ProduitSerializer
	lookup_field = "pk"
	


# @api_view(['GET'])
# # @authentication_classes([SessionAuthentication, BasicAuthentication])
# # @permission_classes([IsAuthenticated])
# @renderer_classes([JSONRenderer])
# def detailCommande(request):
# 	content={
# 		'user': str(request.user),  # `django.contrib.auth.User` instance.
# 		'auth': str(request.auth),  # None
# 	}
# 	print(request.user.client)
# 	if request.user.is_authenticated:
# 		client = request.user.client
# 		commande, created = Commande.objects.get_or_create(client=client, complet=False)
# 		data = commande.orderitem_set.all()
# 		serializer_class = OrderItemSerializer(data, many=True)
# 	else:
# 		{'message': 'pas de user'}
# 	return Response(serializer_class.data)

class UpdateProduitView(generics.UpdateAPIView):
	serializer_class = serializers.ProduitSerializer
	permission_classes = [permissions.IsAdminUser]
	lookup_field='pk'



# @api_view(['UPDATE'])
# def updateItem(request):
# 	a = json.dumps(request.data)
# 	data = json.loads(a)
# 	productId = data['productId']
# 	action = data['action']
# 	print('Action:', action) 
# 	print('Product:', productId)

# 	client = request.user.client
# 	produit = Produit.objects.get(id=productId)
# 	commande, created = Order.objects.get_or_create(customer=customer, complete=False)

# 	orderItem, created = OrderItem.objects.get_or_create(commande=commande, product=product)

# 	if action == 'add':
# 		orderItem.quantite = (orderItem.quantite + 1)
# 	elif action == 'remove':
# 		orderItem.quantite = (orderItem.quantite - 1)

# 	orderItem.save()

# 	if orderItem.quantity <= 0:
# 		orderItem.delete()

# 	return JsonResponse('Item was added', safe=False)

# @api_view(['POST', 'GET'])
# @permission_classes((permissions.AllowAny,))
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def inscription(request):
# 	a = json.dumps(request.data)
# 	data = json.loads(a)

# 	username = data['nom']
# 	email = data['email']
# 	password = data['password']
# 	tel = data['tel']

# 	user = User.objects.create_user(username, email, password)
# 	client, created = Client.objects.get_or_create(user=user, tel=tel)
# 	client.save()
# 	context = {'nom':username, 'email':email, 'tel':tel}
# 	return JsonResponse(context)


class CreateUserView(generics.CreateAPIView):
	serializer_class = serializers.UserSerializer()
	permission_classes = [permissions.IsAuthenticated]


class DetailClientView(generics.RetrieveUpdateAPIView):
	queryset = models.User.objects.all()
	serializer_class = serializers.UserSerializer()
	permission_classes = [permissions.IsAuthenticated]
	lookup_field = "pk"

class MaCommandeView(generics.ListAPIView):
	serializer_class = serializers.ProduitCommandeSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		user = self.request.user
		produits = models.ProduitCommande(client=user)
		return produits