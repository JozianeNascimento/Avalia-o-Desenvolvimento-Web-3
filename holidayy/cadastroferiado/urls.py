from django.urls import path
from . import views


urlpatterns = [
    path('', views.cadastrar, name='cadastroferiado'),
]