# Generated by Django 4.1.7 on 2023-04-07 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0006_deparment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deparment',
            name='department_hod_name',
            field=models.SlugField(max_length=100),
        ),
        migrations.AlterField(
            model_name='deparment',
            name='department_name',
            field=models.CharField(max_length=50),
        ),
    ]