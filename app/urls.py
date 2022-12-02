"""django_course URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views import home, categories, products, customers, orders, users

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home.index, name='home'),
    path('categories/', categories.index, name='categories_index'),
    path('categories/create', categories.create, name='categories_create'),
    path('categories/store', categories.store, name='categories_store'),
    path('categories/edit/<int:id>', categories.edit, name='categories_edit'),
    path('categories/delete/<int:id>', categories.delete, name='categories_delete'),
    
    path('products/', products.index, name='products_index'),
    path('products/create', products.create, name='products_create'),
    path('products/store', products.store, name='products_store'),
    path('products/edit/<int:id>', products.edit, name='products_edit'),
    path('products/delete/<int:id>', products.delete, name='products_delete'),
    
    path('customers/', customers.index, name='customers_index'),
    path('customers/create', customers.create, name='customers_create'),
    path('customers/store', customers.store, name='customers_store'),
    path('customers/edit/<int:id>', customers.edit, name='customers_edit'),
    path('customers/delete/<int:id>', customers.delete, name='customers_delete'),
    
    path('orders/', orders.index, name='orders_index'),
    path('orders/create', orders.create, name='orders_create'),
    path('orders/getProducts', orders.getProducts, name='getProducts'),
    path('orders/getUnitPrice', orders.getUnitPrice, name='getUnitPrice'),
    path('orders/store', orders.store, name='orders_store'),
    
    # users routes
    path('users/', users.index, name='users_index'),
    path('login/', users.user_login, name='users_login'),
    path('register/', users.register, name='users_register'),
    path('users/store', users.store, name='users_store'),
    path('logout/', users.user_logout, name='logout'),

]
