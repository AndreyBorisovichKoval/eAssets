import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    # Настройки SMTP сервера Gmail
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    SMTP_USERNAME = 'notification.sender.57@gmail.com'
    SMTP_PASSWORD = '%#5nV)/(Mxs@9W@'

    # Содержимое письма
    sender = 'notification.sender.57@gmail.com'
    recipient = 'andrey.koval@tcell.tj'
    subject = 'Test Message'
    body = 'Привет! Это тестовое письмо!!!'

    # Создание объекта MIMEText для форматирования письма
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient

    try:
        # Установка соединения с SMTP сервером Gmail
        smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        smtp_server.starttls()

        # Авторизация на SMTP сервере
        smtp_server.login(SMTP_USERNAME, SMTP_PASSWORD)

        # Отправка письма
        smtp_server.sendmail(sender, recipient, message.as_string())

        # Закрытие соединения с SMTP сервером
        smtp_server.quit()

        print('Письмо успешно отправлено!')
    except Exception as e:
        print('Ошибка при отправке письма:', str(e))

# Вызов функции для отправки письма
# send_email()

# =================================================================
# mail.ru

# def send_email():
#     # Настройки SMTP сервера
#     SMTP_SERVER = 'smtp.mail.ru'
#     SMTP_PORT = 465
#     # SMTP_PORT = 587
#     SMTP_USERNAME = 'notification.sender.0@mail.ru'
#     # SMTP_PASSWORD = 'kBRbuXFGAL5Jd1Xdn4zy'
#     SMTP_PASSWORD = '%#5nV)/(Mxs@9W@'
#
#     # Отправитель и получатель
#     SENDER_EMAIL = 'notification.sender.0@mail.ru'
#     RECIPIENT_EMAIL = 'andrey.koval@tcell.tj'
#
#     # Создание MIME объекта
#     message = MIMEMultipart()
#     message['From'] = SENDER_EMAIL
#     message['To'] = RECIPIENT_EMAIL
#     message['Subject'] = 'notification eAssets ReCalculations'
#
#     # Добавление текста письма
#     message.attach(MIMEText('Привет, это пример письма!', 'plain'))
#
#     # Инициализация SMTP соединения
#     # smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#     smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#     smtp_server.starttls()
#     smtp_server.login(SMTP_USERNAME, SMTP_PASSWORD)
#
#     # Отправка письма
#     smtp_server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, message.as_string())
#
#     # Закрытие SMTP соединения
#     smtp_server.quit()
#
# # Вызов функции для отправки письма
# # send_email()

# =================================================================



# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
# def send_email(subject, message, sender_email, recipient_email, smtp_server, smtp_port, smtp_username, smtp_password):
#
#     # Создание MIME объекта
#     email_message = MIMEMultipart()
#     email_message['From'] = sender_email
#     email_message['To'] = recipient_email
#     email_message['Subject'] = subject
#
#     # Добавление текста письма
#     email_message.attach(MIMEText(message, 'plain'))
#
#     # Инициализация SMTP соединения
#     smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
#     smtp_connection.starttls()
#     smtp_connection.login(smtp_username, smtp_password)
#
#     # Отправка письма
#     smtp_connection.sendmail(sender_email, recipient_email, email_message.as_string())
#
#     # Закрытие SMTP соединения
#     smtp_connection.quit()


# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
# # Настройки SMTP сервера
# SMTP_SERVER = 'smtp.mail.ru'
# SMTP_PORT = 465
# SMTP_USERNAME = 'notification.sender.0@mail.ru'
# SMTP_PASSWORD = 'kBRbuXFGAL5Jd1Xdn4zy'
#
# # Отправитель и получатель
# SENDER_EMAIL = 'notification.sender.0@mail.ru'
# RECIPIENT_EMAIL = 'andrey.koval@tcell.tj'
#
# # Создание MIME объекта
# message = MIMEMultipart()
# message['From'] = SENDER_EMAIL
# message['To'] = RECIPIENT_EMAIL
# message['Subject'] = 'notification eAssets ReCalculations'
#
# # Добавление текста письма
# message.attach(MIMEText('Привет, это пример письма!', 'plain'))
#
# # Инициализация SMTP соединения
# smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
# smtp_server.starttls()
# smtp_server.login(SMTP_USERNAME, SMTP_PASSWORD)
#
# # Отправка письма
# smtp_server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, message.as_string())
#
# # Закрытие SMTP соединения
# smtp_server.quit()
#




# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
# # Настройки SMTP сервера
# SMTP_SERVER = 'smtp.example.com'
# SMTP_PORT = 587
# SMTP_USERNAME = 'your_username'
# SMTP_PASSWORD = 'your_password'
#
# # Отправитель и получатель
# SENDER_EMAIL = 'sender@example.com'
# RECIPIENT_EMAIL = 'recipient@example.com'
#
# # Создание MIME объекта
# message = MIMEMultipart()
# message['From'] = SENDER_EMAIL
# message['To'] = RECIPIENT_EMAIL
# message['Subject'] = 'Пример письма'
#
# # Добавление текста письма
# message.attach(MIMEText('Привет, это пример письма!', 'plain'))
#
# # Инициализация SMTP соединения
# smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
# smtp_server.starttls()
# smtp_server.login(SMTP_USERNAME, SMTP_PASSWORD)
#
# # Отправка письма
# smtp_server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, message.as_string())
#
# # Закрытие SMTP соединения
# smtp_server.quit()

