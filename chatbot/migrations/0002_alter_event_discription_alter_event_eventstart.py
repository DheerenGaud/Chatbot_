# Generated by Django 4.1.7 on 2023-03-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Discription',
            field=models.CharField(max_length=122),
        ),
        migrations.AlterField(
            model_name='event',
            name='EventStart',
            field=models.DateTimeField(),
        ),
    ]
