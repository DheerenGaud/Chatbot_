# Generated by Django 4.1.7 on 2023-03-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventName', models.CharField(max_length=122)),
                ('EventStart', models.CharField(max_length=122)),
                ('Discription', models.DateTimeField()),
            ],
        ),
    ]