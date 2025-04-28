from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

desafios_para_cada_mes = {
    "janeiro": "Não beber álcool",
    "fevereiro": "Ir caminhar uma vez por semana",
    "março": "Sair sozinha ao menos 1 vez",
    "abril": "Ir para a academia 3 dias na semana",
    "maio": "Descobrir um novo hobbie",
    "junho": "Encontrar migos de longa data ao menos 1 vez",
    "julho": "Viajar sozinha",
    "agosto": "Caminhar por 20 minutos 3 vezes na semana",
    "setembro": "Não comer carne",
    "outubro": "Visitar um parente distante",
    "novembro": "Ler um livro surpresa",
    "dezembro": None
}

# Create your views here.
def index(request):
    meses = list(desafios_para_cada_mes.keys())

    return render(request, "challenges/index.html", {
        "lista_meses": meses
    })

def desafio_mensal_numerico(request, mes): # 'mes' é o rota na url definida no urlpatterns do App challenges
    try:
        meses = list(desafios_para_cada_mes.keys())
        nome_do_mes = meses[mes-1]
        path_redirecionado = reverse("challenge_path", args=[nome_do_mes]) # challenges/janeiro
        return HttpResponseRedirect(path_redirecionado)
    except:
        return HttpResponseNotFound("Mês inválido :(")

def desafio_mensal(request, mes): 
    try:
        texto_desafio = desafios_para_cada_mes[mes]
        return render(request, "challenges/challenge.html", {
            "nome_mes": mes,
            "desafio": texto_desafio
        })
    except:
        raise Http404() #Vai buscar um arquivo chamado 404.html
        # Debug = False no final de produção para funcionar