# Generated by Django 4.2.11 on 2024-03-14 20:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('date', models.DateField()),
                ('time', models.TimeField(choices=[('17:00', '17:00 PM'), ('18:00', '18:00 PM'), ('19:00', '19:00 PM'), ('20:00', '20:00 PM'), ('21:00', '21:00 PM'), ('22:00', '22:00 PM'), ('23:00', '23:00 PM')], validators=[django.core.validators.RegexValidator(message='Time must be between 5:00 PM and 11:00 PM', regex='^([1][7-9]|20|21|22|23):00$')])),
                ('number_of_people', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)])),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')], default='pending', max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='review',
            old_name='review_text',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='review',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='review',
            name='email',
        ),
    ]
