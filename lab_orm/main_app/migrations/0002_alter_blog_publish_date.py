# Generated by Django 4.2.1 on 2023-05-30 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog", name="publish_date", field=models.DateField(),
        ),
    ]
