# Generated by Django 2.0.7 on 2020-02-25 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeuser', '0002_auto_20200225_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercode',
            name='email',
            field=models.EmailField(max_length=60, unique=True),
        ),
    ]
