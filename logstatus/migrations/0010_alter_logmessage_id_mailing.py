# Generated by Django 5.0.2 on 2024-03-16 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logstatus', '0009_alter_logmessage_id_mailing'),
        ('mailing', '0009_remove_mailing_sending_status_delete_logstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logmessage',
            name='id_mailing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing', verbose_name='Рассылка'),
        ),
    ]
