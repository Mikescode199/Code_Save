# Generated by Django 3.0.3 on 2020-02-13 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codigo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tablatecnicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMBTEC', models.CharField(max_length=30)),
                ('APATTEC', models.CharField(max_length=30)),
                ('AMATTEC', models.CharField(max_length=30)),
                ('TIPOTEC', models.CharField(max_length=30)),
                ('TECINSTAL', models.CharField(max_length=30)),
                ('ANIOCONTTEC', models.IntegerField()),
                ('EMPRTEC', models.CharField(max_length=30)),
                ('ZONATEC', models.CharField(max_length=30)),
                ('REP_INST_TEC', models.CharField(max_length=30)),
                ('NUMTRABTEC', models.IntegerField()),
            ],
        ),
    ]