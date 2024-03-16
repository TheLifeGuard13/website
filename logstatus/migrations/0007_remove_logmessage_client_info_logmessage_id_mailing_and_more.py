# Generated by Django 5.0.2 on 2024-03-16 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logstatus', '0006_alter_logmessage_client_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logmessage',
            name='client_info',
        ),
        migrations.AddField(
            model_name='logmessage',
            name='id_mailing',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Айди_рассылки'),
        ),
        migrations.AlterField(
            model_name='logmessage',
            name='sending_status',
            field=models.CharField(max_length=5, verbose_name='Статус'),
        ),
    ]
