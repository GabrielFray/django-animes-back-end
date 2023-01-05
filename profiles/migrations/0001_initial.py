# Generated by Django 4.1.5 on 2023-01-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('episodes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animes_viewed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('avatar_url', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_episode_viewed', models.TextField()),
                ('animes_viewed', models.ManyToManyField(related_name='profile_viewed', through='profiles.Animes_viewed', to='episodes.episode')),
            ],
        ),
    ]
