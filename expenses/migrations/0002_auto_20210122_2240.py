# Generated by Django 3.1.5 on 2021-01-22 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Main_Category',
            new_name='Mode',
        ),
        migrations.AlterModelOptions(
            name='mode',
            options={'verbose_name_plural': 'Modes'},
        ),
    ]
