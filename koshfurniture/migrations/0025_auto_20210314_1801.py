# Generated by Django 3.1.5 on 2021-03-14 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koshfurniture', '0024_auto_20210313_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
