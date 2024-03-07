# # celery.py
# import os
# from celery import Celery
#
# # Установка переменной окружения для настройки Celery
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
#
# # Создание экземпляра Celery
# app = Celery('your_project')
#
# # Загрузка настроек из файла settings.py Django
# app.config_from_object('django.conf:settings', namespace='CELERY')
#
# # Автоматическое обнаружение и регистрация задач из файлов tasks.py в приложениях Django
# app.autodiscover_tasks()
#
