# Generated by Django 4.2.8 on 2024-01-26 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turnover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(blank=True, max_length=100)),
                ('turnovers', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
