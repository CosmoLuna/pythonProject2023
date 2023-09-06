# Generated by Django 4.2.4 on 2023-09-06 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_voc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pronunciation', models.FileField(upload_to='vocabulary/audio/')),
                ('transcription', models.CharField(max_length=50)),
                ('definition', models.CharField(max_length=100)),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.voc')),
            ],
        ),
    ]