# Generated by Django 4.2 on 2024-09-27 01:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_posts"),
    ]

    operations = [
        migrations.CreateModel(
            name="Work",
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
                ("username", models.CharField(max_length=50)),
                ("startDate", models.CharField(max_length=20)),
                ("startTime", models.CharField(max_length=20)),
                ("endDate", models.CharField(max_length=20)),
                ("endTime", models.CharField(max_length=20)),
                ("maximumEndDate", models.CharField(max_length=20)),
                ("maximumEndTime", models.CharField(max_length=20)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name="posts",
            name="postedCategory",
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
