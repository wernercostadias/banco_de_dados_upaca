# Generated by Django 5.1.2 on 2024-12-07 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0024_alter_pessoa_estudando'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_fotos', models.IntegerField(choices=[(1, '1 Foto'), (2, '2 Fotos'), (3, '3 Fotos')], default=1)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='painel.pessoa')),
            ],
        ),
    ]
