# Generated by Django 5.0.3 on 2024-03-31 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_news_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.CharField(default='', max_length=50, verbose_name='Дата'),
            preserve_default=False,
        ),
    ]