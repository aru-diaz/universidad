# Generated by Django 4.0.4 on 2022-05-29 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Horario', '0005_alter_grupoalumno_idalumno_alter_grupoalumno_idgrupo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='grupoAlumno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Horario.grupo'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='idDocente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Horario.docente'),
        ),
        migrations.DeleteModel(
            name='GrupoAlumno',
        ),
    ]
