# Generated by Django 3.2.6 on 2022-08-31 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatSection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
