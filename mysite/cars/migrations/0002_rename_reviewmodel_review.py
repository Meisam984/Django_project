# Generated by Django 4.2 on 2023-04-05 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ReviewModel",
            new_name="Review",
        ),
    ]
