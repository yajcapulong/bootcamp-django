# Generated by Django 4.2.2 on 2023-06-13 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_alter_tweet_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-createdAt']},
        ),
    ]