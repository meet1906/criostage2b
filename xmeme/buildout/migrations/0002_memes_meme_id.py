# Generated by Django 3.1.6 on 2021-02-07 20:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('buildout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memes',
            name='meme_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
