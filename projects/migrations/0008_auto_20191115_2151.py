# Generated by Django 2.2.7 on 2019-11-15 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20191115_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
