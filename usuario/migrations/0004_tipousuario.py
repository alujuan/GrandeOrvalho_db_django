# Generated by Django 4.2.6 on 2023-10-24 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("GrandeOrvalho", "0010_delete_tipousuario"),
        ("uploader", "0001_initial"),
        ("usuario", "0003_remove_usuario_capa"),
    ]

    operations = [
        migrations.CreateModel(
            name="TipoUsuario",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "capa",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="uploader.image",
                    ),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="GrandeOrvalho.cliente"
                    ),
                ),
                (
                    "funcionario",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="GrandeOrvalho.funcionario",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
            options={
                "verbose_name": "Tipo de usuário",
                "verbose_name_plural": "Tipos de usuários",
            },
        ),
    ]
