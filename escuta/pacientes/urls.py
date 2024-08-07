from django.urls import path
from . import views

urlpatterns = [
    path('', views.busca_paciente, name='busca_paciente'),
    path('realizar_consulta/<int:paciente_id>/', views.realizar_consulta, name='realizar_consulta'),
    path('transcribe_audio/<int:paciente_id>/', views.transcribe_audio, name='transcribe_audio'),
    path('gerar_resumos/', views.gerar_resumos, name='gerar_resumos'),
]
