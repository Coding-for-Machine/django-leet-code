# Generated by Django 5.1.1 on 2024-10-03 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('problems', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Problemtypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Javoblar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('javob', models.TextField()),
                ('problems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.problems')),
            ],
        ),
        migrations.AddField(
            model_name='problems',
            name='problemstypes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.problemtypes'),
        ),
    ]
