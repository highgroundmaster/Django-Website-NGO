# Generated by Django 3.1.4 on 2021-01-11 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nirvata', '0005_auto_20210111_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryphoto',
            name='date',
            field=models.CharField(help_text='DayS Mon YYYY, Ex: 9th Dec 2020', max_length=30, null=True),
        ),
    ]