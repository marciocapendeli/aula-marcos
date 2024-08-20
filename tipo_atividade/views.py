from django.shortcuts import render

# Create your views here.
def cadastro_tipoatividade(request):
    return render(request, 'tipoatividade/cadastroTipoAtividade.html')

def lista_tipoatividade(request):
    return render(request, 'tipoatividade/listarTiposAtividade.html')