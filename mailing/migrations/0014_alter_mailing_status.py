# Generated by Django 5.0.2 on 2024-03-18 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0013_remove_mailing_sending_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[("Создана", "Создана"), ("Запущена", "Запущена"), ("Завершена", "Завершена")],
                default="Готовится",
                max_length=20,
                null=True,
                verbose_name="Статус",
            ),
        ),
    ]
