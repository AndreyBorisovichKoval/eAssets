from django_crontab import CronJobBase
from assets.tasks import my_task


class MyTask(CronJobBase):
    RUN_AT_TIMES = ['00:00']  # Время запуска задачи
    schedule = ' '.join(RUN_AT_TIMES)  # Расписание в формате cron
    code = 'assets.tasks.my_task'  # Уникальный идентификатор задачи

    def do(self):
        my_task()


cron = MyTask()
cron.do()
print('Task Done...')
