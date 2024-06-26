# Generated by Django 5.0.2 on 2024-03-13 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0001_initial"),
        ("letters", "0001_initial"),
        ("mailing", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mailing",
            name="client_emails",
            field=models.ManyToManyField(to="clients.client"),
        ),
        migrations.AddField(
            model_name="mailing",
            name="end_datetime",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Время конца"),
        ),
        migrations.AddField(
            model_name="mailing",
            name="letter_header",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET,
                to="letters.letter",
                verbose_name="Тема письма",
            ),
        ),
        migrations.AddField(
            model_name="mailing",
            name="start_datetime",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Время начала"),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="name",
            field=models.CharField(max_length=150, verbose_name="Имя рассылки"),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="sending_time",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Время рассылки"),
        ),
    ]
