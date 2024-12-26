# Generated by Django 5.1.2 on 2024-12-07 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0023_alter_pessoa_escolaridade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='estudando',
            field=models.CharField(choices=[('nao_estuda', 'Não Estuda'), ('ibraema', 'IBRAEMA'), ('eja_i', 'EJA I'), ('eja_ii', 'EJA II'), ('eja_iii', 'EJA III'), ('ensino_superior', 'Ensino Superior')], max_length=255, null=True),
        ),
    ]