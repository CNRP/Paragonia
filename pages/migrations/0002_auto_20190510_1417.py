# Generated by Django 2.2.1 on 2019-05-10 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='NewsPost',
        ),
        migrations.AlterModelOptions(
            name='newspost',
            options={'verbose_name_plural': 'News'},
        ),
    ]
