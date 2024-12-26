# Generated by Django 5.1.2 on 2024-11-24 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0019_remove_pessoa_data_fim_sancao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eletronico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, choices=[('tv', 'Tv'), ('radio', 'Rádio')], max_length=50)),
                ('data_entrada', models.DateField(blank=True, null=True)),
                ('nova_fiscal', models.FileField(blank=True, null=True, upload_to='eletronicos/fiscais/')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eletronicos', to='painel.pessoa')),
            ],
        ),
    ]