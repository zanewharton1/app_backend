# Generated by Django 5.1.7 on 2025-03-16 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app_backend', '0002_rename_username_logincredentials_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationCredentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
