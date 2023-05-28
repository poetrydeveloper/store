# Generated by Django 4.2.1 on 2023-05-28 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_deliverystore_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='delivery',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='store.deliverystore', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='product',
            name='manual_delivery',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='store.manualdeliverystore', verbose_name='ручной заказ'),
        ),
    ]