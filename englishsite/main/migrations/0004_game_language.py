# Generated by Django 4.2.4 on 2023-09-05 18:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='language',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]