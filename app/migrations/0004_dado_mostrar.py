# Generated by Django 3.2.8 on 2021-10-26 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_dado_serie'),
    ]

    operations = [
        migrations.AddField(
            model_name='dado',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
    ]
