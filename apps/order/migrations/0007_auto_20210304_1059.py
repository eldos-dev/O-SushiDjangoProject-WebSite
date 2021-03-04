# Generated by Django 3.1.7 on 2021-03-04 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_cartitem_final_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='final_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Общая цена'),
        ),
    ]
