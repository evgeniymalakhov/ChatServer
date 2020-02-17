# Generated by Django 3.0.3 on 2020-02-17 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='first', to=settings.AUTH_USER_MODEL)),
                ('second', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='second', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Message')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Created')),
                ('is_readed', models.BooleanField(default=False, verbose_name='Readed')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Room', verbose_name='Room')),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
    ]
