# Generated by Django 5.0.2 on 2024-02-27 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_rename_education_background_delete_experience'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service',
            new_name='Skills',
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
    ]
