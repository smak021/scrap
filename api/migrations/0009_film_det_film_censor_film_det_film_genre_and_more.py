# Generated by Django 4.0.1 on 2022-01-23 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_ft_data_category_name_ft_data_screen_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='film_det',
            name='film_censor',
            field=models.CharField(default='Not Available', max_length=50),
        ),
        migrations.AddField(
            model_name='film_det',
            name='film_genre',
            field=models.CharField(default='Not Available', max_length=50),
        ),
        migrations.AddField(
            model_name='film_det',
            name='film_length',
            field=models.CharField(default='Not Available', max_length=50),
        ),
        migrations.AddField(
            model_name='film_det',
            name='film_story',
            field=models.CharField(default='Not Available', max_length=50),
        ),
    ]
