# Generated by Django 3.1.7 on 2021-03-05 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20210305_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'Новый заказ'), ('Заказ в обработке', 'Заказ в обработке'), ('postponed', 'Отложен'), ('ready_for_delivery', 'Готов к доставке'), ('picked_up_by_courier', 'Взят курьером'), ('delivered', 'Доставляется'), ('completed', 'Выполнен'), ('canceled', 'Отменен')], default='new', max_length=100, verbose_name='Статус заказа'),
        ),
    ]
