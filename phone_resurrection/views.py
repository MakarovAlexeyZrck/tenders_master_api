from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from phone_resurrection.models import PhonesReestr

from phone_resurrection.serializers import PhonesReestrCreate
from phone_resurrection.serializers import PhonesReestrUpdate
from phone_resurrection.serializers import PhonesReestrReadAllRows
from phone_resurrection.serializers import PhonesReestrReadToUpdateRows


class PhonesReestView(APIView):

    """
        Автор:      Макаров Алексей
        Описание:   Представление для работы с таблицей тел. Я определителя
    """

    def get(self, request, id) -> Response:

        """
            Автор:      Макаров Алексей
            Описание:   Выполнение выборки данных из БД
        """

        if id == 0:

            # Выборка данных с номерами телефона для обн. сведений

            phones_rows = PhonesReestr.objects.filter(need_to_update = 1)
            serializer  = PhonesReestrReadToUpdateRows(phones_rows, many = True)

            return Response(
                {
                    "status":  "ok",
                    "fetched": serializer.data
                },
                status = status.HTTP_200_OK
            )

        elif id == 1:

            # Выборка всех данных из таблицы с реестром телефонов

            phones_rows = PhonesReestr.objects.all()
            serializer  = PhonesReestrReadAllRows(phones_rows, many = True)

            return Response(
                {
                    "status":  "ok",
                    "fetched": serializer.data
                },
                status = status.HTTP_200_OK
            )

        return Response(
            {
                "status":  "error"
            },
            status = status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def post(self, request) -> Response:

        """
            Автор:      Макаров Алексей
            Описание:   Создание нового номера телефона для отсл. Я определителя
        """

        serializer = PhonesReestrCreate(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "Новый телефон успешно добавлен"
                },
                status = status.HTTP_200_OK
            )

        return Response(
            {
                "status": "Ошибка создания нового телефона",
                "reason": serializer.errors
            },
            status = status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, id) -> Response:

        """
            Автор:      Макаров Алексей
            Описание:   Изменение записи об отслеж. номере в Я определителе
        """

        phone_row  = PhonesReestr.objects.get(id = id)
        serializer = PhonesReestrUpdate(
            phone_row, data = request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "Информация о телефоне успешно сохранена"
                },
                status = status.HTTP_200_OK
            )

        return Response(
            {
                "status": "Ошибка изменения информации о телефоне",
                "reason": serializer.errors
            },
            status = status.HTTP_400_BAD_REQUEST
        )
