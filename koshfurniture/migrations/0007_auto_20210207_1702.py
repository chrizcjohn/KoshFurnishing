# Generated by Django 3.1.5 on 2021-02-07 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koshfurniture', '0006_auto_20210207_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='discount',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
