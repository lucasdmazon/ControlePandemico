# Generated by Django 3.2.8 on 2021-11-13 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20211112_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dado',
            name='serie',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Serie',
        ),
    ]
