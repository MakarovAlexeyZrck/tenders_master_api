from rest_framework import status

from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from mail_to_supplier.models import SuppliersEmailNotification
from mail_to_supplier.serializers import SuppliersEmailNotificationRead


class NotificationTemplate(APIView):

    """
        Автор:      Макаров Алексей
        Описание:   Генерирование шаблона с уведомлением
                    поставщика об уклонении / отказе от выполнения контракта
    """

    def get(self, request, id) -> Response:

        """
            Автор:      Макаров Алексей
            Описание:   Получение шаблона уведомления поставщика
        """

        email_template = SuppliersEmailNotification.objects.filter(id = id)
        serializer = SuppliersEmailNotificationRead(email_template, many=True)

        return Response(
            {
                "status": "success", 
                "content": serializer.data
            }
        )
