# Generated by Django 4.1.7 on 2024-11-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0004_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Слаг'),
        ),
    ]
