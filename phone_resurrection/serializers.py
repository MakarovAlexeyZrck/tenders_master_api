from rest_framework import fields, serializers

from phone_resurrection.models import PhonesReestr


class PhonesReestrCreate(serializers.ModelSerializer):

    """
        Автор:      Макаров Алексей
        Описание:   Форматирование данных при создании нового телефона
    """

    class Meta:
        model  = PhonesReestr
        fields = ["phone_nums", "phone_desc"]


class PhonesReestrReadToUpdateRows(serializers.ModelSerializer):

    """
        Автор:      Макаров Алексей
        Описание:   Форматирование данных при чтении из реестра
    """

    class Meta:
        model  = PhonesReestr
        fields = ["id", "phone_nums"]


class PhonesReestrReadAllRows(serializers.ModelSerializer):

    """
        Автор:      Макаров Алексей
        Описание:   Форматирование данных при чтении всех записей из реестра
    """

    class Meta:
        model  = PhonesReestr
        fields = "__all__"


class PhonesReestrUpdate(serializers.ModelSerializer):

    """
        Автор:      Макаров Алексей
        Описание:   Форматирование данных при обновлении инф. о телефоне
    """

    class Meta:
        model  = PhonesReestr
        fields = ["det_polar", "det_status", "det_verdict", "det_desc"]
