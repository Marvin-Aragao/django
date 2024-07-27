from .models import Aluno
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404

def alunoView(request):
    aluno_lista = Aluno.objects.all()
    return render(request, 'main/aluno.html',{'aluno_lista':aluno_lista})

def alunoIDview(request, id):
    aluno = get_object_or_404(Aluno, pk = id)
    return render(request, 'main/alunoID.html', {'aluno':aluno})