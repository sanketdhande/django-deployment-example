# Generated by Django 2.0.5 on 2018-08-06 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_userprofileinfo_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='bio',
            field=models.CharField(max_length=200),
        ),
    ]