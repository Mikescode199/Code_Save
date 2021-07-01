# Generated by Django 3.2.4 on 2021-06-21 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='privacidad',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='codigo_foto',
            field=models.ImageField(blank=True, upload_to='media/images'),
        ),
    ]