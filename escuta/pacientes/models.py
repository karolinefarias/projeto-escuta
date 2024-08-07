from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    duracao = models.CharField(max_length=20)
    transcricao = models.TextField()
    queixa_principal = models.TextField(blank=True, null=True)
    historia_doenca_atual = models.TextField(blank=True, null=True)
    historia_patologica_pregressa = models.TextField(blank=True, null=True)
    cirurgias_realizadas = models.TextField(blank=True, null=True)
    medicamentos_suplementos = models.TextField(blank=True, null=True)
    historia_fisiologica = models.TextField(blank=True, null=True)
    historia_familia = models.TextField(blank=True, null=True)
    historia_social = models.TextField(blank=True, null=True)
    hipoteses_diagnosticas = models.TextField(blank=True, null=True)
    exame_fisico = models.TextField(blank=True, null=True)
    resultado_exames = models.TextField(blank=True, null=True)
    conduta_terapeutica = models.TextField(blank=True, null=True)
    exames_solicitados = models.TextField(blank=True, null=True)
    medicamentos_prescritos = models.TextField(blank=True, null=True)
    observacoes_adicionais = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Consulta de {self.paciente.nome} - {self.duracao}"
