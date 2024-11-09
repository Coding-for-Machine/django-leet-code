# Generated by Django 5.1.2 on 2024-11-09 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coursecategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Dasturlash Tilini yoki Boshqa', max_length=250)),
                ('body', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Dasturlash Tilini yoki Boshqa', max_length=250)),
                ('body', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coursecategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursapp.coursecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Mavzu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Dasturlash Tilini yoki Boshqa', max_length=250)),
                ('body', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursapp.bob')),
            ],
        ),
        migrations.CreateModel(
            name='Mavzutanasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Dasturlash Tilini yoki Boshqa', max_length=250)),
                ('body', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursapp.bob')),
            ],
        ),
    ]
