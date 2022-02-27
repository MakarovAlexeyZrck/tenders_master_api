from django.db import models
from django.utils import timezone


class SuppliersEmailNotification(models.Model):

    """
        Автор:      Макаров Алексей
        Описание:   Таблица с шаблонами email - уведомлений клиентам
    """

    email_template = models.TextField()
    email_recipients = models.CharField(max_length = 1000)
    email_status =  models.SmallIntegerField(default = 0)
    manager_email =  models.CharField(max_length = 1000)
    ts = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = "suppliers_email_notification"
        managed = False
