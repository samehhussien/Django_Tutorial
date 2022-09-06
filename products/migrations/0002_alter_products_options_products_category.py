# Generated by Django 4.0.6 on 2022-07-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['-price'], 'verbose_name': 'product'},
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.CharField(blank=True, choices=[('phone', 'phone'), ('computer', 'computer'), ('screens', 'screens')], max_length=50, null=True),
        ),
    ]
