# Generated by Django 3.1.7 on 2021-04-15 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0004_remove_story_num_clues'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='num_clues',
            field=models.IntegerField(null=True),
        ),
    ]
