# Generated by Django 5.1.2 on 2024-11-19 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0013_remove_pessoa_data_fim_sancao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='data_fim_sancao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='data_inicio_sancao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='sancao_disciplinar',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='sancao_disciplinar_descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='tipo_sancao',
            field=models.CharField(blank=True, choices=[('sem_castelo', 'Sem Castelo'), ('sem_visita_intima', 'Sem Visita Íntima'), ('sem_visita_social', 'Sem Visita Social')], max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='SancaoDisciplinar',
        ),
    ]
