# Generated by Django 4.2.4 on 2023-08-27 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_employee_gender"),
    ]

    operations = [
        migrations.CreateModel(
            name="Type",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "Type",
                "verbose_name_plural": "Types",
            },
        ),
        migrations.AddField(
            model_name="employee",
            name="type",
            field=models.ForeignKey(
                default=2, on_delete=django.db.models.deletion.CASCADE, to="app.type"
            ),
            preserve_default=False,
        ),
    ]
