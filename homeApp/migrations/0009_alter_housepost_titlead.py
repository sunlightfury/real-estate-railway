# Generated by Django 3.2.6 on 2022-07-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0008_alter_housepost_bedroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housepost',
            name='titleAd',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
