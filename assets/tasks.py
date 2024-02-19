from datetime import datetime, timedelta, date
from decimal import Decimal
# from django.db.models import F

from assets.models import Asset, TaskCheckPoint


def recalculate_assets():
    try:
        task_check_point = TaskCheckPoint.objects.get(title='Assets Recalculation')
        last_processed_date = task_check_point.last_processed_date
        is_successful = task_check_point.is_successful

        if last_processed_date.month != datetime.now().month or last_processed_date.year != datetime.now().year or not is_successful:
            task_check_point.is_successful = False  # Устанавливаем значение 0 в поле is_successful
            task_check_point.save()

            assets = Asset.objects.filter(is_written_off=False)

            # current_date = datetime.now()
            # months_passed = (current_date.year - F('acquisition_date__year')) * 12 + (
            #             current_date.month - F('acquisition_date__month'))
            # depreciation_per_month = F('cost') / (F('service_life') * 12)
            # remaining_cost = F('cost') - (depreciation_per_month * months_passed)
            #
            # Asset.objects.filter(is_written_off=False).update(
            #     current_cost=remaining_cost,
            #     last_recalculation_date=current_date
            # )

            for asset in assets:
                acquisition_date = asset.acquisition_date
                # Вычисляем количество месяцев между датой приобретения и текущей датой
                months_passed = (datetime.now().year - acquisition_date.year) * 12 + (
                    datetime.now().month - acquisition_date.month)
                # Вычисляем остаточную стоимость
                depreciation_per_month = asset.cost / (asset.service_life * 12)
                remaining_cost = asset.cost - (depreciation_per_month * months_passed)
                # Обновляем поле current_cost актива
                asset.current_cost = Decimal(remaining_cost)
                asset.last_recalculation_date = datetime.now()
                asset.save()

            task_check_point.last_processed_date = datetime.now()
            task_check_point.is_successful = True  # Устанавливаем значение 1 в поле is_successful
            task_check_point.save()

    except TaskCheckPoint.DoesNotExist:
        # Запись TaskCheckPoint не найдена
        return TaskCheckPoint.DoesNotExist
