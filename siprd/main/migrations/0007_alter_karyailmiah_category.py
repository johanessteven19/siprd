# Generated by Django 3.2.7 on 2021-12-02 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20211106_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='karyailmiah',
            name='category',
            field=models.TextField(),
        ),
    ]
