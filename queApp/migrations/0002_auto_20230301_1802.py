# Generated by Django 3.1 on 2023-03-01 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='view',
            name='isRecommended',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Is recommended'),
        ),
        migrations.AddField(
            model_name='view',
            name='isTopTen',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Is top ten'),
        ),
    ]