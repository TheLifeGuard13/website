# Generated by Django 5.0.2 on 2024-03-16 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("logstatus", "0010_alter_logmessage_id_mailing"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="logmessage",
            name="server_answer",
        ),
    ]
