# Generated by Django 3.0.6 on 2020-05-06 07:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('topicApp', '0002_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]