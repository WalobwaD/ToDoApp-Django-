# Generated by Django 4.1.1 on 2022-09-27 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0007_alter_todo_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 27, 15, 52, 2, 505113)),
        ),
    ]
