from django.urls import path
from . import views

urlpatterns = [
    path("", views.index), # /challenge/
    path("<int:mes>", views.desafio_mensal_numerico),
    path("<str:mes>", views.desafio_mensal, name="challenge_path")
]