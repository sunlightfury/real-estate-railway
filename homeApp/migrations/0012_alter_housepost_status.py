# Generated by Django 3.2.6 on 2022-07-14 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0011_alter_housepost_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housepost',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Desactive', 'Desactive')], default='Active', max_length=50),
        ),
    ]