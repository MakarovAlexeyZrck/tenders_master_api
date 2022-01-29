from datetime import datetime

from django.template  import loader
from django.shortcuts import render
from django.http      import HttpResponse

from rest_framework.views    import APIView
from rest_framework.response import Response


class RejectionTemplate(APIView):

    """
        Автор:      Макаров Алексей
        Описание:   Шаблон письма - уведомления об уклонение поставщика
    """

    def __init__(self) -> None:

        """
            Автор:      Макаров Алексей
            Описание:   Инициализация класса по рендер. шаблона для уклонения
        """

        self.template = loader.get_template("rejection.html")

    def post(self, request) -> HttpResponse:

        """
            Автор:      Макаров Алексей
            Описание:   Рендер страницы с шаблоном письма об
                        уклонении поставщика от выполнения контракта
        """

        context  = {
            "customer_name":         request.POST["customer_name"],
            "purchase_number":       request.POST["purchase_number"],
            "contact_manager_name":  request.POST["contact_manager_name"],
            "contact_manager_email": request.POST["contact_manager_email"],
            "contact_manager_phone": request.POST["contact_manager_phone"],
        }

        return HttpResponse(self.template.render(context, request))


class TerminationTemplate(APIView):

    """
        Автор:      Макаров Алексей
        Описание:   Шаблон письма - уведомления о расторжении контракта
    """

    def __init__(self) -> None:

        """
            Автор:      Макаров Алексей
            Описание:   Инициализация класса по рендер. шаблона для расторжения
        """

        self.template = loader.get_template("termination.html")

    def post(self, request) -> HttpResponse:

        """
            Автор:      Макаров Алексей
            Описание:   Рендер страницы с шаблоном письма об
                        одностороннем расторжении заказчика от контракта
        """

        context  = {
            "customer_name":         request.POST["customer_name"],
            "purchase_number":       request.POST["purchase_number"],
            "contact_manager_name":  request.POST["contact_manager_name"],
            "contact_manager_email": request.POST["contact_manager_email"],
            "contact_manager_phone": request.POST["contact_manager_phone"],
        }

        return HttpResponse(self.template.render(context, request))
