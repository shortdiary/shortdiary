# Generated by Django 3.1.7 on 2021-04-27 18:27

import diary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0008_auto_20210427_0543'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaryuser',
            name='include_in_leaderboard',
            field=models.BooleanField(default=True, verbose_name='Include in leaderboard'),
        ),
        migrations.AlterField(
            model_name='diaryuser',
            name='email_verified',
            field=models.BooleanField(default=False, verbose_name='Email verified?'),
        ),
        migrations.AlterField(
            model_name='diaryuser',
            name='language',
            field=models.CharField(default='en_US', max_length=5, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='diaryuser',
            name='last_seen_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Last seen at'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(validators=[diary.models.Post.validate_date], verbose_name='date'),
        ),
    ]