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

