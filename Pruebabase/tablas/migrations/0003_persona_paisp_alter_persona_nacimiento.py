# Generated by Django 4.1.2 on 2022-10-06 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablas', '0002_pais_remove_persona_nacionalidad_remove_persona_pais'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='paisp',
            field=models.CharField(default=True, max_length=100, verbose_name='paisp'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='nacimiento',
            field=models.DateTimeField(verbose_name='nacimiento'),
        ),
    ]
