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


class NotificationSupplierRejection(APIView):

     """
         Автор:      Макаров Алексей
         Описание:   Генерирование шаблона с уведомлением
                     поставщика об уклонении / отказе от выполнения контракта
     """

     def __init__(self) -> None:

         """
             Автор:      Макаров Алексей
             Описание:   Инициализация класса по созданию письма - уведомления
         """

         self.template = loader.get_template("rejection.html")

     def post(self, request) -> Response:

         """
             Автор:      Макаров Алексей
             Описание:   Получение шаблона письма с уведомлением поставщика
         """

         context = {
             "supplier_name": request.POST["supplier_name"],
             "customer_name": request.POST["customer_name"],
             "purchase_number": request.POST["purchase_number"],
             "contact_manager_name": request.POST["contact_manager_name"],
             "contact_manager_email": request.POST["contact_manager_email"],
             "contact_manager_phone": request.POST["contact_manager_phone"],
         }

         return HttpResponse(self.template.render(context, request))


class NotificationSupplierTermination(APIView):

     """
         Автор:      Макаров Алексей
         Описание:   Генерирование шаблона с уведомлением
                     поставщика об уклонении / отказе от выполнения контракта
     """

     def __init__(self) -> None:

         """
             Автор:      Макаров Алексей
             Описание:   Инициализация класса по созданию письма - уведомления
         """

         self.template = loader.get_template("termination.html")

     def post(self, request) -> Response:

         """
             Автор:      Макаров Алексей
             Описание:   Получение шаблона письма с уведомлением поставщика
         """

         context = {
            "supplier_name": request.POST["supplier_name"],
            "customer_name": request.POST["customer_name"],
            "purchase_number": request.POST["purchase_number"],
            "contact_manager_name": request.POST["contact_manager_name"],
            "contact_manager_email": request.POST["contact_manager_email"],
            "contact_manager_phone": request.POST["contact_manager_phone"],
         }

         return HttpResponse(self.template.render(context, request))


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

        print(id)

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

        self.recipient_copies += [serializer.data[0]["manager_email"]]

        recipients = [
            i["recipient"] for i in json.loads(
                request.POST["recipients_emails"])
        ]

        email_template = SuppliersEmailNotification.objects.filter(
            id = request.POST["notification_id"])
        serializer = SuppliersEmailNotificationRead(email_template, many = True)

        for i in recipients:
            self.smtp_server.send_email(
                "Уведомление от ЕИС", serializer.data[0]["email_template"], i)
            for i1 in self.recipient_copies:
                self.smtp_server.send_email(
                    "Уведомление от ЕИС", serializer.data[0]["email_template"], i1)

        return Response(
            {
                "status": "success"
            }
        )
