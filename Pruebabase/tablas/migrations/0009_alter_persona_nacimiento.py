# Generated by Django 4.1.2 on 2022-10-06 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablas', '0008_alter_persona_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='nacimiento',
            field=models.DateTimeField(verbose_name='nacimiento (yyyy-mm-dd)'),
        ),
    ]