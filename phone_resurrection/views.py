from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect
from rest_framework.views import APIView

from phone_resurrection.models import PhonesReestr

from phone_resurrection.serializers import PhonesReestrCreate
from phone_resurrection.serializers import PhonesReestrReadFullTable
from phone_resurrection.serializers import PhonesReestrUpdateAfterCheck


def fetch_on_phone_state(request, state: str):

    """
        Автор:      Макаров Алексей
        Описание:   Выборка номеров телефонов согласно их статусу в Я определ.
    """

    rows = PhonesReestr.objects.filter(phone_state=state)
    formated_rows = PhonesReestrReadFullTable(rows, many=True)

    return JsonResponse(
        {"data": formated_rows.data}, status=status.HTTP_200_OK)


def fetch_on_phone_update_status(request, phone_update_status: int):

    """
        Автор:      Макаров Алексей
        Описание:   Выборка номеров телефонов для проверки статуса в Я определ.
    """

    rows = PhonesReestr.objects.filter(need_to_update=phone_update_status)
    formated_rows = PhonesReestrReadFullTable(rows, many=True)

    return JsonResponse(
        {"data": formated_rows.data}, status=status.HTTP_200_OK)


class PhonesReestView(APIView):

    """
        Автор:      Макаров Алексей
        Описание:   Взаимодействие с реестром телефонов и их проверками в Я
    """

    def get(self, request) -> Response:

        """
            Автор:      Макаров Алексей
            Описание:   Выборка всех данных из таблицы с реестром телефонов
        """

        rows = PhonesReestr.objects.all()
        serializer = PhonesReestrReadFullTable(rows, many = True)

        return Response(
            {"fetched": serializer.data}, status = status.HTTP_200_OK)

    def post(self, request) -> Response:

        """
            Автор:      Макаров Алексей
            Описание:   Выполнение запроса по добавлению данных в реестр
        """

        serializer = PhonesReestrCreate(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "ok"}, status = status.HTTP_200_OK)

        return Response(
            {
                "status": "error", "reason": serializer.errors
            },
            status = status.HTTP_400_BAD_REQUEST)

    def patch(self, request, phone_id: int) -> Response:

        """
            Автор:      Макаров Алексей
            Описание:   Изменение записи об отслеж. номере в Я определителе
        """

        phone_row = PhonesReestr.objects.get(id=phone_id)
        serializer = PhonesReestrUpdateAfterCheck(phone_row, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "ok"}, status=status.HTTP_200_OK)

        return Response(
            {"status": "error", "reason": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
