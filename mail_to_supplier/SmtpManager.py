import smtplib
from email.mime.text import MIMEText


class SmtpManager():

    """
        Автор:      Макаров Алексей
        Описание:   Подключение к почтовому SMTP серверу
    """

    def __init__(self) -> None:

        """
            Автор:      Макаров Алексей
            Описание:   Инициализация класса по работе с SMTP серверу
        """

        self.smtp_server = None

        self.user_login = "eis.news.sender@gmail.com"
        self.user_password = "qwerty077"

        self.__create_smtp_connection()

    def __create_smtp_connection(self) -> None:

        """
            Автор:      Макаров Алексей
            Описание:   Создание соединения с почтовым сервером
        """

        self.smtp_server = smtplib.SMTP("smtp.gmail.com", 587, timeout = 10)

        self.smtp_server.starttls()
        self.smtp_server.login(self.user_login, self.user_password)

    def send_email(
        self, message_header: str, message_text: str, recipient: str) -> int:

        """
            Автор:      Макаров Алексей
            Описание:   Метод для отправки электронного сообщения адресанту
        """

        message_template = MIMEText(message_text, "html", "utf-8")

        message_template["From"] = "Уведомление ЕИС"
        message_template["Subject"] = message_header

        self.smtp_server.sendmail(
            self.user_login, recipient, message_template.as_string())

        return 0
