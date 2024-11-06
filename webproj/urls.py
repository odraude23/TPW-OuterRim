"""webproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('favourites/', views.favourites, name='favourites'),

    path('register/', views.register, name='register'),

    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('cart/', views.cart, name='cart'),
    path('following/', views.following, name='following'),
    path('myproducts/', views.myproducts, name='myproducts'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('editproduct/<int:product_id>/', views.edit_product, name='editproduct'),
    path('admin-page/', views.admin_page, name='admin_page'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('checkout/', views.checkout, name='checkout'),


    # remover
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('messages/', views.messages_page, name='messages_page'),
    path('messages/<int:user_id>/', views.messages_page, name='messages_page'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


