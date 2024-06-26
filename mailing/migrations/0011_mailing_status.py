# Generated by Django 5.0.2 on 2024-03-16 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0010_alter_mailing_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="mailing",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[("Готовится", "Готовится"), ("Успешно", "Успешно"), ("Безуспешно", "Безуспешно")],
                max_length=20,
                null=True,
                verbose_name="Статус",
            ),
        ),
    ]
