# Generated by Django 3.0.7 on 2020-10-17 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('squirrels', '0003_squirrel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='date',
            field=models.DateField(auto_now_add=True, help_text='Day the Squirrel was Sighted'),
        ),
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('squirrel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='squirrels.Squirrel')),
            ],
        ),
    ]
