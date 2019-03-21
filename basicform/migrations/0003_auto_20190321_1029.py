# Generated by Django 2.1.7 on 2019-03-21 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicform', '0002_userprofileinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='picture',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics/'),
        ),
    ]
