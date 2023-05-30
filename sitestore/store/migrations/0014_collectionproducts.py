# Generated by Django 4.2.1 on 2023-05-30 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_mainpage_alter_tools_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('note', models.TextField(blank=True, max_length=250, null=True, verbose_name='Описание')),
                ('quantity', models.PositiveIntegerField(null=True, verbose_name='Количество в магазине.')),
                ('products', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='store.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Ед.т.',
                'verbose_name_plural': 'Ед.т.',
                'ordering': ['created_at'],
            },
        ),
    ]