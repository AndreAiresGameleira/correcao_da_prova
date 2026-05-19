from django.urls import path, include
from . import views

app_name = 'livros'

urlpatterns = [
    path('lista/', views.lista_view, name='lista'),
    path('detalhes/', views.detalhes_view, name='detalhes'),

]
