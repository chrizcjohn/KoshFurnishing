from django.urls import path ,include
from . import views
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout")
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
