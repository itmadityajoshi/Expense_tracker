# Generated by Django 4.2.3 on 2023-07-30 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_profile_expenses'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
