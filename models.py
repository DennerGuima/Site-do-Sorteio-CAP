import email
from django.db import models

# Create your models here.
class Clientes(models.Model):
    SEXO = (
            ('M', 'Masculino'),
            ('F', 'Feminino'),
    )

    TURMA = (
            ('1', '1º ano'),
            ('2', '2º ano'),
            ('3', '3º ano'),
            ('4', '4º ano'),
            ('5', '5º ano'),
            ('6', '6º ano'),
            ('7', '7º ano'),
            ('8', '8º ano'),
    )




    cpf = models.CharField('Digite seu cpf', max_length = 11, default='')
    dn = models.CharField('Data de nascimento', max_length = 10, default='')
    rua = models.CharField('Digite sua rua', max_length = 200, default='')
    numero = models.CharField('Numero da casa', max_length = 5, default='')
    bairro = models.CharField('Bairro', max_length = 200, default='')
    turma = models.CharField('Turma', max_length = 1, choices= TURMA)
    nome_resp = models.CharField('Nome do responsavel', max_length = 200, default='')
    sexo = models.CharField('Sexo', max_length = 1, choices= SEXO)
    telefone = models.CharField('Telefone', max_length = 15, default='')
    email = models.CharField('Digite seu email', max_length = 200, default='')


    def __str__(self):
        return self.nome 