# Generated by Django 4.1.7 on 2023-04-01 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_alter_event_discription_alter_event_eventstart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newevent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=122)),
                ('eventurl', models.URLField()),
                ('eventstart', models.DateTimeField()),
                ('discription', models.CharField(max_length=122)),
                ('eventend', models.DateTimeField()),
                ('eventlogo', models.CharField(max_length=122)),
            ],
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
