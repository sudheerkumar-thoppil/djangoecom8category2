# Generated by Django 3.0.5 on 2023-04-01 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop9', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Category_name',
            new_name='category_name',
        ),
    ]