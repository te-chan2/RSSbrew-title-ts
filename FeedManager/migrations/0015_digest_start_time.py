# Generated by Django 5.0.6 on 2024-05-29 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeedManager', '0014_alter_processedfeed_last_digest'),
    ]

    operations = [
        migrations.AddField(
            model_name='digest',
            name='start_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
