# Generated by Django 3.0 on 2020-06-22 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20200622_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='qno',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
