# Generated by Django 4.2.1 on 2023-05-14 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_provider_alter_tools_options_alter_tools_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Бренд')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='tools',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='store.provider', verbose_name='Поставщик'),
        ),
        migrations.AddField(
            model_name='tools',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='store.brand', verbose_name='Бренд'),
        ),
    ]
