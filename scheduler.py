# import os
# import django
# from django.conf import settings
# from datetime import datetime
# import schedule
# import time
# from tasks import recalculate_assets
# from assets.models import *
#
#
# def run_scheduler():
#     # Установить переменную окружения DJANGO_SETTINGS_MODULE
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eAssets.settings')
#
#     # Инициализировать настройки Django
#     django.setup()
#
#     # Запланировать выполнение задачи раз в месяц в полночь
#     schedule.every().month.do(recalculate_assets)
#
#     # Бесконечный цикл для выполнения запланированных задач
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
#
# if __name__ == "__main__":
#     # Конфигурирование настроек Django
#     settings.configure()
#
#     run_scheduler()
