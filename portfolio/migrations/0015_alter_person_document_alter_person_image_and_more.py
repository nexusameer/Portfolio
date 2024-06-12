# Generated by Django 5.0.2 on 2024-06-11 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_person_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='document',
            field=models.FileField(upload_to='portfolio/'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(upload_to='portfolio/'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image1',
            field=models.ImageField(upload_to='portfolio/'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image2',
            field=models.ImageField(upload_to='portfolio/'),
        ),
    ]
