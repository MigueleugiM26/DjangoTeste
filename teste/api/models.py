from django.db import models
import string
import random

def generateCode():
    length = 8

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Home.objects.filter(code=code).count() == 0:
            break;

    return code

class Home(models.Model): 
    code = models.CharField(max_length=10, default=generateCode, unique=True, verbose_name="Código")
    password = models.CharField(max_length=12, default="", verbose_name="Senha")
    mistakes = models.IntegerField(null=False, default=6, verbose_name="Erros")
    spaces = models.BooleanField(null=False, default=False, verbose_name="Permitir espaços")
    tips = models.BooleanField(null=False, default=True, verbose_name="Permitir dicas")
    created_at = models.DateTimeField(auto_now_add=True)
