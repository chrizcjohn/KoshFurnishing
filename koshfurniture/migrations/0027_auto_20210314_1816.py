# Generated by Django 3.1.5 on 2021-03-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koshfurniture', '0026_auto_20210314_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
