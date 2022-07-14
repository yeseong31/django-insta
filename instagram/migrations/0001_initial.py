# Generated by Django 4.0.6 on 2022-07-14 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField()),
                ('content', models.TextField()),
                ('image', models.TextField()),
                ('profile_image', models.TextField()),
                ('like_count', models.IntegerField()),
            ],
        ),
    ]
