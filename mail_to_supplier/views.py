import json

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from mail_to_supplier.SmtpManager import SmtpManager


class MailToSupplier(APIView):

    """
        Автор:      Макаров Алексей
        Описание:   Интерфейс для отправки электронного письма
                    на адрес электронной почты поставщика
    """

    def __init__(self) -> None:

        """
            Автор:      Макаров Алексей
            Описание:   Инициализация класса по отправке эл. письма клиенту
        """

        self.mail_server = SmtpManager()

        self.recipients_list = ["mak_alexey@icloud.com"]
        # self.recipients_list = ["akulov@trade.su"]

    def post(self, request) -> Response:

        """

            Автор:      Макаров Алексей
            Описание:   Отправляет сообщение на электронную почту клиента

        """

        self.recipients_list += json.loads(request.POST["recipients"])

        for recipient in self.recipients_list:
            # send mail
            pass


        return Response({"status": 1})
