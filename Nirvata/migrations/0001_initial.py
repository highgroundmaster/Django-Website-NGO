# Generated by Django 3.1.4 on 2021-01-10 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=1000, null=True)),
                ('title', models.CharField(max_length=20, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('date', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]