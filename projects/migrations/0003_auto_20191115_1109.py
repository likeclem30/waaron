# Generated by Django 2.2.7 on 2019-11-15 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20191115_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='static/img'),
        ),
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.CharField(max_length=600),
        ),
    ]
