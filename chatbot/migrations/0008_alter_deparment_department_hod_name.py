# Generated by Django 4.1.7 on 2023-04-07 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0007_alter_deparment_department_hod_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deparment',
            name='department_hod_name',
            field=models.CharField(max_length=100),
        ),
    ]