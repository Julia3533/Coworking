# Generated by Django 5.0.1 on 2024-02-05 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('COWORKINGS', '0003_remove_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='COWORKINGS.project'),
        ),
    ]
