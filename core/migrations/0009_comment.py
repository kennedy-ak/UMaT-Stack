# Generated by Django 4.1.7 on 2023-03-16 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_delete_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_name", models.CharField(max_length=20)),
                ("user_email", models.EmailField(max_length=254)),
                ("text", models.TextField(max_length=300)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="core.post",
                    ),
                ),
            ],
        ),
    ]
