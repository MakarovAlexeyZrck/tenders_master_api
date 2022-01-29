from django.db import models
from django.utils import timezone


class PhonesReestr(models.Model):

    """
        Автор:      Макаров Алексей
        Описание:   Реестр телефонов и информация о них в Я определителе
    """

    phone_desc      = models.CharField(max_length = 100)
    phone_nums      = models.CharField(max_length = 100, unique = True)

    det_polar       = models.CharField(max_length = 100, default = "check_need")
    det_status      = models.CharField(max_length = 100, default = "check_need")
    det_verdict     = models.CharField(max_length = 100, default = "check_need")
    det_desc        = models.CharField(max_length = 100, default = "check_need")

    time_updated    = models.DateTimeField(auto_now = True)
    time_created    = models.DateTimeField(auto_now_add = True)

    need_to_update = models.SmallIntegerField(default = 1)

    class Meta:
        db_table = "phones_reestr"
