# Generated by Django 3.2.3 on 2021-05-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mshall', '0002_champs2011to2012sports_champs2012to2013socult_champs2016to2017sports_champs2017to2018sports_champs20'),
    ]

    operations = [
        migrations.AddField(
            model_name='champs2011to2012sports',
            name='roll',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='champs2012to2013socult',
            name='roll',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='champs2016to2017sports',
            name='roll',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='champs2017to2018sports',
            name='roll',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='champs2018to2019sports',
            name='roll',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='champs2019to2020socult',
            name='roll',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='champs2019to2020tech',
            name='roll',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='champs2020to2021tech',
            name='roll',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
