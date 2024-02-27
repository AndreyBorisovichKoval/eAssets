# import os
# import django
# from datetime import datetime, timedelta, date
# from decimal import Decimal
# from assets.models import Asset, TaskCheckPoint
# import schedule
# import time
#
#
# # # Установка переменной окружения DJANGO_SETTINGS_MODULE
# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eAssets.settings.py')
# #
# # # Инициализация Django
# # django.setup()
#
#
# def recalculate_assets():
#     try:
#         task_check_point = TaskCheckPoint.objects.get(title='Assets Recalculation')
#         last_processed_date = task_check_point.last_processed_date
#         is_successful = task_check_point.is_successful
#
#         current_date = datetime.now().date()
#
#         if (last_processed_date.month != current_date.month or
#                 last_processed_date.year != current_date.year or
#                 not is_successful):
#             task_check_point.is_successful = False
#             task_check_point.save()
#
#             assets = Asset.objects.filter(is_written_off=False)
#
#             for asset in assets:
#                 acquisition_date = asset.acquisition_date
#                 months_passed = (current_date.year - acquisition_date.year) * 12 + (
#                     current_date.month - acquisition_date.month)
#                 depreciation_per_month = asset.cost / (asset.service_life * 12)
#                 remaining_cost = asset.cost - (depreciation_per_month * months_passed)
#                 asset.current_cost = Decimal(remaining_cost)
#                 asset.last_recalculation_date = current_date
#                 asset.save()
#
#             task_check_point.last_processed_date = current_date
#             task_check_point.is_successful = True
#             task_check_point.save()
#
#     except TaskCheckPoint.DoesNotExist:
#         return TaskCheckPoint.DoesNotExist
#
#
# schedule.every().hour.at(":15").do(recalculate_assets)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
#
#
