# Generated by Django 4.1.2 on 2022-10-06 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablas', '0007_remove_persona_idp_alter_persona_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='nacimiento',
            field=models.DateField(verbose_name='nacimiento (yyyy-mm-dd)'),
        ),
    ]
