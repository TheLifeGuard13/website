# Generated by Django 5.0.2 on 2024-04-06 15:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("header", models.CharField(max_length=100, verbose_name="Заголовок")),
                ("description", models.TextField(blank=True, null=True, verbose_name="Содержимое")),
                ("preview", models.ImageField(blank=True, null=True, upload_to="blogs/", verbose_name="Изображение")),
                ("views_count", models.IntegerField(default=0, verbose_name="Просмотры")),
                ("published_at", models.DateField(auto_now_add=True, null=True, verbose_name="Дата публикации")),
                ("slug", models.CharField(blank=True, max_length=100, null=True, verbose_name="Читабельная ссылка")),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Владелец",
                    ),
                ),
            ],
            options={
                "verbose_name": "запись",
                "verbose_name_plural": "записи",
            },
        ),
    ]
