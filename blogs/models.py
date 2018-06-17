from django.db import models

class Blog(models.Model):
    pergunta = models.CharField(max_length=300)
    resposta = models.TextField()

    def __str__(self):
        return self.pergunta

