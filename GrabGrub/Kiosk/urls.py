from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('view_customer', views.view_customer, name='view_customer'),
    path('view_orders/', views.view_orders, name='view_orders'),
    path('view_details/<int:pk>/', views.view_details, name='view_details'),
    path('update_details/<int:pk>/', views.update_details, name='update_details'),
    path('view_food/', views.view_food, name='view_food'),
    path('view_customers/', views.view_customers, name='view_customers'),
    path('add_customer/',views.add_customer, name='add_customer'),
    path('update_customer/<int:pk>/', views.update_customer,name='update_customer'),
    path('delete_customer/<int:pk>/', views.delete_customer, name='delete_customer'),
    path('add_food/', views.add_food, name='add_food'),
    path('delete_order/<int:pk>/', views.delete_order, name='delete_order'),
    path('add_order/',views.add_order, name='add_order'),
    path('delete_food/<int:pk>/', views.delete_food, name='delete_food'),
    path('update_food/<int:pk>/', views.update_food, name='update_food'),
]
