from django.urls import path
from . import views

urlpatterns = [
    path('<str:string>/', views.word, name ='word'),
    path('',views.home, name = 'home'),
    path('<str:string>/confirm', views.confirm, name = 'confirm')
]
