from django.shortcuts import render


def lista_view(request):
    return render(request, 'livros/lista.html')

def detalhes_view(request):
    return render(request, 'livros/detalhes.html')