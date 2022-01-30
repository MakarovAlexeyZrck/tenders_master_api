from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response

from phone_resurrection.models import PhonesReestr

from phone_resurrection.serializers import PhonesReestrReadFullTable



def fetch_on_phone_state(request, state: str) -> Response:

    """
        Автор:      Макаров Алексей
        Описание:   Выборка номеров телефонов согласно их статусу в Я определ.
    """

    rows = PhonesReestr.objects.filter(phone_state = state)
    formated_rows = PhonesReestrReadFullTable(rows, many = True)

    return JsonResponse(
        {
            "data": formated_rows.data
        },
        status = status.HTTP_200_OK
    )


def fetch_on_phone_update_status(request, phone_update_status: int) -> Response:

    """
        Автор:      Макаров Алексей
        Описание:   Выборка номеров телефонов для проверки статуса в Я определ.
    """

    rows = PhonesReestr.objects.filter(need_to_update = phone_update_status)
    formated_rows = PhonesReestrReadFullTable(rows, many = True)

    return JsonResponse(
        {
            "data": formated_rows.data
        },
        status = status.HTTP_200_OK
    )
