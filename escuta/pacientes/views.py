from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Paciente, Consulta
from .forms import ConsultaForm
import requests
import assemblyai as aai
import openai
from django.http import JsonResponse
import json
from decouple import AutoConfig
from hugchat import hugchat
from hugchat.login import Login

config = AutoConfig(search_path='.')

# Configure sua chave de API
openai.api_key = config('OPENAI_API_KEY')
aai.settings.api_key = config('AA_API_KEY') 

# Log in to huggingface and grant authorization to huggingchat
EMAIL = config('EMAIL_HUGCHAT')
PASSWD = config('PASSWD_HUGCHAT')
cookie_path_dir = "../cookies/" # NOTE: trailing slash (/) is required to avoid errors
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

@csrf_exempt
def gerar_resumos(request):
    if request.method == 'POST':
        transcricao = request.POST.get('transcricao')
        if transcricao:
            # Preparar a solicitação para a API do ChatGPT
            prompt = f"""
            A partir do seguinte texto transcrito, gere resumos para os seguintes campos:
            - Queixa Principal
            - História da Doença Atual
            - História Patológica Pregressa
            - Cirurgias Realizadas
            - Medicamentos e suplementos em uso atualmente
            - História fisiológica
            - História familiar
            - História social
            - Hipóteses diagnósticas
            - Exame Físico
            - Resultado de exames
            - Conduta terapêutica
            - Exames solicitados
            - Medicamentos prescritos

            A resposta deve ser para cada campo uma linha, separando cada item da resposta por :
            Texto transcrito:
            {transcricao}
            """
            # response = openai.completions.create(
            #     model="gpt-3.5-instruct",  # Você pode usar outro modelo se preferir
            #     prompt=prompt,
            #     max_tokens=1500,
            #     temperature=0.5
            # )
            # Create your ChatBot
            chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

            message_result = chatbot.chat(prompt)
            resumos = message_result.text.strip()
            
            # Separar os resumos em campos
            campos = resumos.split('\n')
            resultado = {}
            for campo in campos:
                if ':' in campo:
                    chave, valor = campo.split(':', 1)
                    resultado[chave.strip('-').strip('*').strip()] = valor.strip('*').strip()
            return JsonResponse(resultado)
        return JsonResponse({'error': 'Erro ao gerar resumos'}, status=400)
    return JsonResponse({'error': 'Método não permitido'}, status=405)

def busca_paciente(request):
    query = request.GET.get('q')
    pacientes = Paciente.objects.all()
    if query:
        pacientes = pacientes.filter(nome__icontains=query)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        paciente_list = list(pacientes.values('id', 'nome', 'idade'))
        return JsonResponse({'pacientes': paciente_list})
    
    return render(request, 'pacientes/busca_paciente.html', {'pacientes': pacientes})

def realizar_consulta(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        consulta = Consulta(
            paciente=paciente,
            duracao=request.POST.get('duracao', ''),
            transcricao=request.POST.get('transcricao', ''),
            queixa_principal=request.POST.get('queixa_principal', ''),
            historia_doenca_atual=request.POST.get('historia_doenca_atual', ''),
            historia_patologica_pregressa=request.POST.get('historia_patologica_pregressa', ''),
            cirurgias_realizadas=request.POST.get('cirurgias_realizadas', ''),
            medicamentos_suplementos=request.POST.get('medicamentos_suplementos', ''),
            historia_fisiologica=request.POST.get('historia_fisiologica', ''),
            historia_familia=request.POST.get('historia_familia', ''),
            historia_social=request.POST.get('historia_social', ''),
            hipoteses_diagnosticas=request.POST.get('hipoteses_diagnosticas', ''),
            exame_fisico=request.POST.get('exame_fisico', ''),
            resultado_exames=request.POST.get('resultado_exames', ''),
            conduta_terapeutica=request.POST.get('conduta_terapeutica', ''),
            exames_solicitados=request.POST.get('exames_solicitados', ''),
            medicamentos_prescritos=request.POST.get('medicamentos_prescritos', ''),
            observacoes_adicionais=request.POST.get('observacoes_adicionais', '')
        )
        consulta.save()
        return redirect('busca_paciente')
    
    return render(request, 'pacientes/realizar_consulta.html', {'paciente': paciente})

def transcribe_audio(request, paciente_id):
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']

        config = aai.TranscriptionConfig(language_code="pt")
        transcriber = aai.Transcriber(config=config)
        transcript = transcriber.transcribe(audio_file)

        if transcript.status == aai.TranscriptStatus.error:
            transcricao = f"Transcrição falhou: {transcript.error}"
        else:
            transcricao = transcript.text

        return JsonResponse({'transcricao': transcricao})
    return JsonResponse({'error': 'Invalid request'}, status=400)
