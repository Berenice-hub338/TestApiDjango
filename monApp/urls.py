from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProduitListView.as_view(), name="vitrine"),
    path('detail-produit/<int:pk>/', views.DetailProduitView.as_view(), name="detail_produit"),
    path('ma-commande/', views.MaCommandeView.as_view(), name="ma_commande"),
    path('update-produit/<int:pk>', views.UpdateProduitView.as_view(), name="update_produit"),
    path('client/', views.CreateUserView.as_view() , name="inscription_client"),
    path('detail-client/<int:pk>/',views.DetailClientView.as_view(), name="detail_client")
]
