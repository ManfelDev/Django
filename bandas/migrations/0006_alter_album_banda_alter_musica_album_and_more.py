# Generated by Django 5.1.3 on 2025-03-27 11:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bandas", "0005_alter_musica_album"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="banda",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="albuns",
                to="bandas.banda",
            ),
        ),
        migrations.AlterField(
            model_name="musica",
            name="album",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="albuns",
                to="bandas.album",
            ),
        ),
        migrations.AlterField(
            model_name="musica",
            name="banda",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="musicas",
                to="bandas.banda",
            ),
        ),
    ]
