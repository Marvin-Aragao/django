from django.urls import path
from . import views

urlpatterns = [
    path('', views.alunoView, name='aluno_lista'),
    path('alunoID/<int:id>', views.alunoIDview, name='aluno_detalhe'),
]
