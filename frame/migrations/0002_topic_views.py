# Generated by Django 2.2.1 on 2019-05-10 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frame', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
