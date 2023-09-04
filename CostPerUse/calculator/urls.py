from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator, name='calculator'),
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
]