# Generated by Django 5.1.2 on 2024-11-16 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0005_alter_pessoa_frente_trabalho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='frente_trabalho',
            field=models.CharField(choices=[('nao_trabalha', 'Não trabalha'), ('horta', 'Horta'), ('piscicultura', 'Piscicultura'), ('minhocario', 'Minhocário'), ('limpeza', 'Limpeza'), ('manutencao', 'Manutenção'), ('fabrica_blocos', 'Fábrica de Blocos'), ('croche', 'Crochê')], max_length=20),
        ),
    ]