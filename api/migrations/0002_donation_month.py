# Generated by Django 4.2 on 2024-10-05 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="donation",
            name="month",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
