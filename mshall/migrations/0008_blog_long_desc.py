# Generated by Django 4.1.2 on 2022-11-12 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mshall", "0007_blog"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog", name="long_desc", field=models.TextField(default=""),
        ),
    ]
