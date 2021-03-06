# Generated by Django 3.0 on 2020-07-02 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20200623_0533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='question',
        ),
        migrations.AddField(
            model_name='option',
            name='questions',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='options', to='quiz.Questions'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questions',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='quiz.Quiz'),
        ),
    ]
