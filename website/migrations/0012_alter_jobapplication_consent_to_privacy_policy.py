# Generated by Django 5.1.1 on 2024-09-19 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_jobapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='consent_to_privacy_policy',
            field=models.BooleanField(null=True),
        ),
    ]
