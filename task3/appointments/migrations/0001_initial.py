# Generated by Django 4.1 on 2023-04-25 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('require', models.CharField(max_length=200, null=True)),
                ('description', models.TextField()),
                ('start_time', models.DateField()),
                ('end_time', models.TimeField()),
            ],
        ),
    ]
