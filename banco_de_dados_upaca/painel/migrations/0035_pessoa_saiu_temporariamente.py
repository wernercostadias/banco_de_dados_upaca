# Generated by Django 5.1.2 on 2024-12-24 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0034_pessoa_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='saiu_temporariamente',
            field=models.BooleanField(default=False),
        ),
    ]