# Generated by Django 2.2.6 on 2019-10-03 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191003_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
