import json
from rest_framework import status

from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from mail_to_supplier.models import SuppliersEmailNotification
from mail_to_supplier.serializers import SuppliersEmailNotificationRead
from mail_to_supplier.serializers import NotificationSaveRecipients
from mail_to_supplier.serializers import NotificationManagerRecipient

from mail_to_supplier.SmtpManager import SmtpManager


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


class SendNotificationTemplate(APIView):

    """
        Автор:      Макаров Алексей
        Описание:   Отправляем шаблон с уведомлением
                    поставщика об уклонении / отказе от выполнения контракта
    """

    def __init__(self) -> None:

        """
            Автор:      Макаров Алексей
            Описание:   Инициализация класса
        """

        self.smtp_server = SmtpManager()
        self.recipient_copies = ["mak_alexey@icloud.com"]

    def post(self, request) -> HttpResponse:

        """
            Автор:      Макаров Алексей
            Описание:   Выполнение рассылки клиентам
        """

        manager_email = SuppliersEmailNotification.objects.filter(
            id = request.POST["notification_id"])
        serializer = NotificationManagerRecipient(manager_email, many = True)

        print(serializer.data)

        recipients = [
            i["recipient"] for i in json.loads(request.POST["recipients_emails"])
        ] + self.recipient_copies

        email_template = SuppliersEmailNotification.objects.filter(
            id = request.POST["notification_id"])
        serializer = SuppliersEmailNotificationRead(email_template, many = True)

        for i in recipients:
            self.smtp_server.send_email(
                "Уведомление от ЕИС", serializer.data[0]["email_template"], i)

        return Response(
            {
                "status": "success"
            }
        )
