# Generated by Django 2.2.1 on 2019-05-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20190510_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='text',
            field=models.TextField(),
        ),
    ]
