# Generated by Django 4.0.1 on 2022-01-16 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_ft_data_options_ft_data_film_loc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ft_data',
            options={'ordering': ('show_date', 'theatre_id')},
        ),
        migrations.AddField(
            model_name='film_det',
            name='image_url',
            field=models.CharField(default='none', max_length=5),
        ),
    ]
