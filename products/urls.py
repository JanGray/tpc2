
from django.urls import path

from . import views
app_name = 'products'

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="catalog"),
	path('view/', views.store1, name="catalog1"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('items/<slug:slug>/',views.product_about ,name='details')

]
