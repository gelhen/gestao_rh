# Generated by Django 2.2 on 2020-01-29 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0002_registro_hora_extra_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro_hora_extra',
            name='horas',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]
