# Generated by Django 5.0.2 on 2024-02-27 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_blog_admin_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='education',
            name='person',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='person',
        ),
        migrations.RemoveField(
            model_name='service',
            name='person',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
