# Generated by Django 5.0.2 on 2024-03-16 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0011_mailing_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[("Готовится", "Готовится"), ("Успешно", "Успешно"), ("Безуспешно", "Безуспешно")],
                default="Готовится",
                max_length=20,
                null=True,
                verbose_name="Статус",
            ),
        ),
    ]
