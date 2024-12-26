# Generated by Django 5.1.2 on 2024-11-19 23:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0015_transferencia_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='tipo_sancao',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Sancao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, choices=[('sem_castelo', 'Sem Castelo'), ('sem_visita_intima', 'Sem Visita Íntima'), ('sem_visita_social', 'Sem Visita Social')], max_length=50)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_inicio', models.DateTimeField(blank=True, null=True)),
                ('data_fim', models.DateTimeField(blank=True, null=True)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sancoes', to='painel.pessoa')),
            ],
        ),
    ]
