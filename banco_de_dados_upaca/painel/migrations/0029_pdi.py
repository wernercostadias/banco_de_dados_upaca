# Generated by Django 5.1.2 on 2024-12-11 21:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0028_alter_pessoa_frente_trabalho'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('natureza', models.CharField(blank=True, choices=[('leve', 'Natureza Leve'), ('media', 'Natureza Média'), ('grave', 'Natureza Grave')], max_length=50)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_inicio', models.DateTimeField(blank=True, null=True)),
                ('data_fim', models.DateTimeField(blank=True, null=True)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pd_is', to='painel.pessoa')),
            ],
        ),
    ]
