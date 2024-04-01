from django.urls import path
from . import views

urlpatterns = [
    path('',views.sign,name='signin'),
    path("login",views.login_user,name='login'),
    path('home',views.home,name='home')
]

