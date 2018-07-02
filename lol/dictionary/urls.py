from django.urls import path
from . import views

urlpatterns = [
    path('<str:string>/', views.word, name='word'),
]
