# Generated by Django 3.1.2 on 2020-10-21 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrels', '0009_auto_20201019_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='latitude',
            field=models.DecimalField(decimal_places=15, max_digits=17, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='longitude',
            field=models.DecimalField(decimal_places=15, max_digits=17, null=True),
        ),
    ]
