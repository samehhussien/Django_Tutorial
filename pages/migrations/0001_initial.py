# Generated by Django 4.0.6 on 2022-07-12 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='female',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_female', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='male',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_male', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.female')),
            ],
        ),
    ]
