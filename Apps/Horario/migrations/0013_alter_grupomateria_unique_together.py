# Generated by Django 4.0.4 on 2022-05-29 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Horario', '0012_alter_grupo_iddocente'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='grupomateria',
            unique_together={('idGrupo', 'idMateria')},
        ),
    ]
