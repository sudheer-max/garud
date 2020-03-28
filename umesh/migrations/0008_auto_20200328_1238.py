# Generated by Django 3.0.4 on 2020-03-28 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umesh', '0007_domestic_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='slug',
            field=models.SlugField(default='match'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='international',
            name='slug',
            field=models.SlugField(default='next'),
            preserve_default=False,
        ),
    ]
