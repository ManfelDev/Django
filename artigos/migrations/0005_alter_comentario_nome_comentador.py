# Generated by Django 5.1.3 on 2025-03-29 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artigos", "0004_remove_autor_nome_utilizador"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comentario",
            name="nome_comentador",
            field=models.CharField(max_length=100, verbose_name="Nome do comentador"),
        ),
    ]
