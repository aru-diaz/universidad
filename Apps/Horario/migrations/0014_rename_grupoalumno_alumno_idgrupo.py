# Generated by Django 4.0.4 on 2022-06-03 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Horario', '0013_alter_grupomateria_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='grupoAlumno',
            new_name='idGrupo',
        ),
    ]
