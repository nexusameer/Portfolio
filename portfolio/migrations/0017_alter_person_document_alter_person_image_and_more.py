# Generated by Django 5.0.2 on 2024-06-11 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_alter_person_document_alter_person_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='document',
            field=models.FileField(upload_to='portfolio/documents/'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(upload_to='portfolio/images/'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image1',
            field=models.ImageField(upload_to='portfolio/images/'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image2',
            field=models.ImageField(upload_to='portfolio/images/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(upload_to='portfolio/images/'),
        ),
    ]
