# Generated by Django 4.1.2 on 2022-11-11 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mshall", "0006_auto_20210711_1558"),
    ]

    operations = [
        migrations.CreateModel(
            name="blog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Title", models.CharField(max_length=1000)),
                ("img", models.ImageField(upload_to="pictures")),
                ("desc", models.TextField()),
            ],
        ),
    ]