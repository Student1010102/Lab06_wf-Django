# Generated by Django 4.1.7 on 2024-11-24 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique_for_date='pub_date', verbose_name='Слаг'),
        ),
    ]
