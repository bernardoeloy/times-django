from django.db import models
 
 
class Time(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    criado_em = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.nome
 
    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'