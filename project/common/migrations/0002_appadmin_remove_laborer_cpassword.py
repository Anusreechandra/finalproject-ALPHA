# Generated by Django 4.0.3 on 2022-03-29 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppAdmin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'appadmin',
            },
        ),
        migrations.RemoveField(
            model_name='laborer',
            name='cpassword',
        ),
    ]
