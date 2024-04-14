# Generated by Django 5.0.2 on 2024-03-18 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0012_alter_mailing_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mailing",
            name="sending_time",
        ),
        migrations.AddField(
            model_name="mailing",
            name="first_sending_time",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Время первой рассылки"),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name="Время создания"),
        ),
    ]
