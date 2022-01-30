from django.db import models
from django.utils import timezone


class PhonesReestr(models.Model):

    """
    Автор:      Макаров Алексей
    Описание:   Реестр телефонов и информация о них в Я определителе
    """

    phone_numbs  = models.CharField(max_length = 100, unique = True)

    phone_state  = models.CharField(max_length = 100, default = "check_need")
    phone_descr  = models.CharField(max_length = 100, default = "check_need")

    time_updated = models.DateTimeField(auto_now = True)
    time_created = models.DateTimeField(auto_now_add = True)

    update_need  = models.SmallIntegerField(default = 1)

    class Meta:
        db_table = "phones_reestr"
