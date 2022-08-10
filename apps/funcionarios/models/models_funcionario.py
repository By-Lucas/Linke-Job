from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from empresas.models.models_empresa import Empresa

# Create your models here.
class Funcionario(models.Model):
    CARGOS_CHOICES = (
        ('PP', 'Desenvolvedor Python Pleno'),
        ('PJ', 'Desenvolvedor Python Júnior'),
        ('JS', 'Desenvolvedor Java Script Pleno'),
        ('C', 'CEO'),
        ('RC', 'Tech Recruiter'),
        ('RS', 'Desenvolvedor React Sênior'),
        ('O', 'Outros'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    empresa = models.ManyToManyField(Empresa)
    cargo = models.CharField(choices=CARGOS_CHOICES, null=True, blank=True, max_length=100)

    def __str__(self):
        return self.nome


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.is_staff:
        try:
            group = Group.objects.get(name='admin')
        except:
            group = Group.objects.create(name='admin')
    else:
        try:
            group = Group.objects.get(name='funcionario')
        except:
            group = Group.objects.create(name='funcionario')

    instance.groups.add(group)
    #if created:
    #    Funcionario.objects.create(user=instance)

#AQUI SALVA TODAS AS INFORMACOES DO PERFIL INFORMADO ACIMA
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()