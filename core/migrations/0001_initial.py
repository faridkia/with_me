# Generated by Django 5.0.4 on 2024-05-01 23:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(choices=[('sh', 'شاد'), ('na', 'ناامید'), ('ta', 'غم'), ('gh', 'طبیعی')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='books/images/', verbose_name='عکس')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=500)),
                ('author', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('feeling', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='core.feeling')),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(upload_to='audios/audios/')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='audios/images/')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('score', models.PositiveSmallIntegerField()),
                ('feeling', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.feeling')),
            ],
        ),
        migrations.CreateModel(
            name='PodcastComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد شده')),
                ('text', models.CharField(max_length=300, verbose_name='متن')),
                ('is_published', models.BooleanField(default=False, verbose_name='منتشر')),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.podcast')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='core.podcastcomment', verbose_name='ریپلای')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنت پادکست ها',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('audio', models.FileField(upload_to='songs/audios/')),
                ('image', models.ImageField(upload_to='songs/images/')),
                ('singer', models.CharField(max_length=50)),
                ('feeling', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='podcasts', to='core.feeling')),
            ],
        ),
        migrations.CreateModel(
            name='AudioComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد شده')),
                ('text', models.CharField(max_length=300, verbose_name='متن')),
                ('is_published', models.BooleanField(default=False, verbose_name='منتشر')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='core.audiocomment', verbose_name='ریپلای')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.song')),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنت اهنگ ها',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos/')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('feeling', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='videos', to='core.feeling')),
            ],
        ),
    ]
