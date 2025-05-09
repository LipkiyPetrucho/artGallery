# Generated by Django 5.1.3 on 2025-04-22 20:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0002_alter_painting_options_painting_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='image',
            field=models.ImageField(upload_to='paintings/', verbose_name='Главное изображение'),
        ),
        migrations.CreateModel(
            name='PaintingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='paintings/', verbose_name='Дополнительный ракурс')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('painting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_images', to='artworks.painting', verbose_name='Картина')),
            ],
            options={
                'verbose_name': 'Доп. изображение',
                'verbose_name_plural': 'Доп. изображения',
                'ordering': ['order'],
            },
        ),
    ]
