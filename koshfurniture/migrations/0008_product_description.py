# Generated by Django 3.1.5 on 2021-02-07 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koshfurniture', '0007_auto_20210207_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
