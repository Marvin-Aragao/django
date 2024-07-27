from .models import Aluno
from django.http import HttpResponse
from django.shortcuts import render

def alunoView(request):
    aluno_lista = Aluno.objects.all()
    return render(request, 'main/aluno.html',{'aluno_lista':aluno_lista})
