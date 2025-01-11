# orders/signals.py

from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Order, OrderStatusHistory

@receiver(pre_save, sender=Order)
def track_order_status_change(sender, instance, **kwargs):
    if not instance.pk:
        # Новый заказ, не нужно отслеживать изменение статуса
        return

    try:
        previous = Order.objects.get(pk=instance.pk)
    except Order.DoesNotExist:
        return

    if previous.status != instance.status:
        # Статус изменен, создаем запись в истории
        OrderStatusHistory.objects.create(
            order=instance,
            status=instance.status,
            changed_by=instance.user  # Или другой источник информации о пользователе
        )
