from django.db import models

# Create your models here.


class categoria(models.Model):
    nome = models.CharField(max_length=100)
    # o comando auto_now_add=true pega a data actual do momento da criacao
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):

        return self.nome


class Transacao(models.Model):
    descricao = models.CharField(max_length=100)
    data = models.DateTimeField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categor = models.ForeignKey(categoria, on_delete=models.CASCADE)
    observacao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Transações"

    def __str__(self):

        return self.descricao
