# Generated by Django 5.0.2 on 2024-03-14 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0002_mailing_client_emails_mailing_end_datetime_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="period",
            field=models.CharField(
                choices=[("Ежедневно", "Ежедневно"), ("Еженедельно", "Еженедельно"), ("Ежемесячно", "Ежемесячно")],
                max_length=150,
                verbose_name="Период",
            ),
        ),
        migrations.DeleteModel(
            name="Period",
        ),
    ]
