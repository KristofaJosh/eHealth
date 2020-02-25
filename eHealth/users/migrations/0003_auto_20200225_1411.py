# Generated by Django 3.0.3 on 2020-02-25 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200225_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalinformation',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicalinformation',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='medicalinformation',
            name='marital_status',
            field=models.CharField(choices=[('SI', 'Single'), ('MA', 'Married'), ('DI', 'Divorce')], max_length=2),
        ),
    ]
