# Generated by Django 5.1.1 on 2024-09-20 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_alter_jobapplication_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='email_address',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
