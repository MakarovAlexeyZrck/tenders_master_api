import json

from django.template import loader
from rest_framework import status
from django.shortcuts import render
from django.http      import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response


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
                    поставщика об одностороннем расторжении контракта
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
