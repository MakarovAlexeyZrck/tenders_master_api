from rest_framework import fields, serializers

from phone_resurrection.models import PhonesReestr


class PhonesReestrReadFullTable(serializers.ModelSerializer):

    """
        Автор:      Макаров Алексей
        Описание:   Форматирование данных при чтении из реестра 
    """

    class Meta:
        model = PhonesReestr
        fields = "__all__"


class PhonesReestrUpdateAfterCheck(serializers.ModelSerializer):

    """
        Автор:      Макаров Алексей
        Описание:   Форматирование данных при обновлении инф. после пров. в Я
    """

    class Meta:
        model = PhonesReestr
        fields = ["phone_state", "phone_descr"]


class PhonesReestrCreate(serializers.ModelSerializer):

    """
        Автор:      Макаров Алексей
        Описание:   Форматирование данных при создании телефона для проверок
    """

    class Meta:
        model  = PhonesReestr
        fields = ["phone_numbs"]
