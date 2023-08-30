# Generated by Django 3.2.3 on 2021-05-22 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mshall', '0004_gcnotices_gnrlnotices_hallnotices_messnotices'),
    ]

    operations = [
        migrations.CreateModel(
            name='alumnid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll', models.CharField(blank=True, max_length=10, null=True)),
                ('Name', models.CharField(max_length=100)),
                ('dept', models.CharField(blank=True, max_length=5, null=True)),
                ('degree', models.CharField(blank=True, max_length=50, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='phdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll', models.CharField(blank=True, max_length=10, null=True)),
                ('Name', models.CharField(max_length=100)),
                ('dept', models.CharField(blank=True, max_length=5, null=True)),
                ('degree', models.CharField(blank=True, max_length=50, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ugd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll', models.CharField(blank=True, max_length=10, null=True)),
                ('Name', models.CharField(max_length=100)),
                ('dept', models.CharField(blank=True, max_length=5, null=True)),
                ('degree', models.CharField(blank=True, max_length=50, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
