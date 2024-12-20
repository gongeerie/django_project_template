# Generated by Django 3.0.11 on 2024-11-24 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='created date')),
                ('modified', models.DateTimeField(blank=True, editable=False, verbose_name='modified date')),
                ('name', models.CharField(max_length=100, verbose_name='category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
