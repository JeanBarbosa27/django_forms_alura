from django.urls import path
from passagens.views.index_view import IndexView
from passagens.views.revisao_consulta_view import RevisaoConsultaView

urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('minha_consulta', RevisaoConsultaView.as_view(), name='minha_consulta'),
]
