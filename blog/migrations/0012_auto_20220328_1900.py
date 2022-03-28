# Generated by Django 3.1.7 on 2022-03-28 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20220317_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, max_length=500, verbose_name='Про себе'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='blog/static/img/profile/default_avatar.jpg', upload_to='blog/static/img/profiles', verbose_name='Картинка профілю'),
        ),
    ]
