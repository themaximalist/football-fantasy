# Generated by Django 3.2.6 on 2021-09-01 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_player_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
