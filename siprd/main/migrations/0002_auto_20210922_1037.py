# Generated by Django 3.2.7 on 2021-09-22 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nip',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='university',
            field=models.CharField(default='testUni', max_length=254),
            preserve_default=False,
        ),
    ]
