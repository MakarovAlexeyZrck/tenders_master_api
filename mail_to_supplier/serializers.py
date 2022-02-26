from rest_framework import fields, serializers

from mail_to_supplier.models import SuppliersEmailNotification


class SuppliersEmailNotificationRead(serializers.ModelSerializer):

    """
        Автор:      Макаров Алексей
        Описание:   Форматирование данных при чтении шаблона уведомления 
    """

    class Meta:
        model  = SuppliersEmailNotification
        fields = ["email_template"]