# Generated by Django 3.2.15 on 2022-08-13 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0006_vagas_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagas',
            name='faixa_salarial',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]