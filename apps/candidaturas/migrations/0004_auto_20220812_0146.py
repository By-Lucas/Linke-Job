# Generated by Django 3.2.15 on 2022-08-12 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0005_vagas_tipo'),
        ('candidaturas', '0003_alter_candidatura_vaga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatura',
            name='vaga',
        ),
        migrations.AddField(
            model_name='candidatura',
            name='vaga',
            field=models.ManyToManyField(to='vagas.Vagas'),
        ),
    ]
