# Generated by Django 3.2.15 on 2022-08-12 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0004_vagas_senioridade'),
    ]

    operations = [
        migrations.AddField(
            model_name='vagas',
            name='tipo',
            field=models.CharField(blank=True, choices=[('HO', 'Home Office'), ('HI', 'Hibrido'), ('PR', 'Presencial')], max_length=20, null=True),
        ),
    ]
