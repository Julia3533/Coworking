# Generated by Django 5.0.1 on 2024-02-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('COWORKINGS', '0004_alter_task_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='project',
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
