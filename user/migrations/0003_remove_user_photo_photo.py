# Generated by Django 5.1.3 on 2024-11-24 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='photos/default.jpg', upload_to='photos/%Y/%m/%d')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='user.user')),
            ],
        ),
    ]
