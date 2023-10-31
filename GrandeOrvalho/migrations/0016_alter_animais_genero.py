# Generated by Django 4.2.6 on 2023-10-27 14:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("GrandeOrvalho", "0015_remove_animais_tipo_animal"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animais",
            name="genero",
            field=models.IntegerField(choices=[(1, "Macho"), (2, "Fêmea")], default=1, verbose_name="Gênero"),
        ),
    ]
