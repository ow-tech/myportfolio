# Generated by Django 3.0.6 on 2020-06-13 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favourite', '0004_auto_20200613_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_disc',
            name='project_dname',
            field=models.CharField(default='nothing', max_length=50),
        ),
    ]