# Generated by Django 5.0.2 on 2024-02-27 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_person_com_projects_alter_person_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='desc',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
