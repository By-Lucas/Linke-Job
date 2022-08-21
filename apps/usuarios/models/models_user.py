from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


def upload_to(instance ,filename):
    return 'user/{username}/{filename}'.format(
        username=instance.user.username, filename=filename)

    def __str__(self):
        return self.escolaridade

class ProfileUser(models.Model):
    TIPO_USUARIO = (
        ('U', 'Usuario'),
        ('E', 'Empresa'),
    )
    UF_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernanbuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_tipo = models.CharField(choices=TIPO_USUARIO, max_length=20, null=True, blank=True, db_column='user_tipo', default='U')
    escolaridade_user = models.CharField(max_length=40, null=True, blank=True, db_column='escolaridade_user')
    idade = models.IntegerField(null=True, blank=True, default=0, db_column='idade')
    cidade = models.CharField(max_length=20, choices=UF_CHOICES, null=True, blank=True, db_column='cidade')
    contato = models.CharField(max_length=11, null=True, blank=True, db_column='contato')
    endereco = models.CharField(max_length=20, null=True, blank=True, db_column='endereco')
    numero_casa = models.IntegerField(null=True, blank=True, db_column='numero_casa')
    cpf = models.CharField(max_length=14, null=True, blank=True, db_column='cpf')
    cnpj = models.CharField(max_length=18, null=True, blank=True, db_column='cnpj')
    sobre = models.TextField(max_length=500, null=True, blank=True, db_column='sobre')
    github_user = models.CharField(max_length=100, null=True, blank=True, db_column='github_user')
    linkedin_user = models.CharField(max_length=100, null=True, blank=True, db_column='linkedin_user')
    instagram_user = models.CharField(max_length=100, null=True, blank=True, db_column='instagram_user')
    imagem_perfil = models.ImageField(default='usuario.png', upload_to=upload_to, null=True, blank=True, db_column='imagem_perfil')
    data_cadastro = models.DateField(null=True, blank=True, auto_created=True, auto_now=True, db_column='data_cadastro')
    data_update = models.DateTimeField(auto_now=True, db_column='data_update')

    def get_user_tipo(self):
        if self.user_tipo == 'U':
            tipo_user = 'Usuario'
        if self.user_tipo == 'E':
            tipo_user = 'Empresa'
        return tipo_user

    class Meta:
        db_table = 'profile_user'
        verbose_name = 'ProfileUser'
        verbose_name_plural = 'ProfileUsers'
    
    def __str__(self):
        return self.user.username 

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        ProfileUser.objects.create(user=instance)