# Generated by Django 3.2.1 on 2021-06-01 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0016_convert_part_of_to_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='part_of',
        ),
    ]
