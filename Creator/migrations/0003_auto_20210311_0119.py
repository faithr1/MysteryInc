# Generated by Django 3.1.7 on 2021-03-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0002_auto_20210310_0429'),
    ]

    operations = [
        migrations.AddField(
            model_name='clue',
            name='clue_img',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='clue',
            name='clue_text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='password', max_length=100),
        ),
    ]
