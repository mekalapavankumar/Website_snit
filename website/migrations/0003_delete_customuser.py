# Generated by Django 5.1.1 on 2024-09-15 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_customuser_user_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
