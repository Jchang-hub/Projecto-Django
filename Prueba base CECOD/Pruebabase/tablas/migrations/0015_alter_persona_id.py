# Generated by Django 4.1.2 on 2022-10-12 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablas', '0014_alter_persona_paisp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
