# from django_crontab import CronJobBase
# from assets.tasks import recalculate_assets
#
#
# class MyTask(CronJobBase):
#     RUN_AT_TIMES = ['00:00']  # Время запуска задачи
#     schedule = ' '.join(RUN_AT_TIMES)  # Расписание в формате cron
#     code = 'assets.tasks.recalculate_asset_current_cost'  # Уникальный идентификатор задачи
#
#     def do(self):
#         recalculate_assets()
#
#
# cron = MyTask()
# cron.do()
# print('Task Done...')
