# Generated by Django 4.0.6 on 2022-07-12 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_test_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='created',
            field=models.DateTimeField(null=True),
        ),
    ]
