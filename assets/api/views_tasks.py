import logging
from datetime import datetime
from decimal import Decimal
from assets.models import Asset, TaskCheckPoint
# from additional.email_sender import send_email


logger = logging.getLogger('application')


class AssetRecalculator:
    def __init__(self):
        self.task_title = 'Assets Recalculation'

    def recalculate_assets(self):
        # send_email()

        try:
            task_check_point = TaskCheckPoint.objects.get(title=self.task_title)
            last_processed_date = task_check_point.last_processed_date
            is_successful = task_check_point.is_successful

            current_date = datetime.now().date()

            if (last_processed_date.month != current_date.month or
                    last_processed_date.year != current_date.year or
                    not is_successful):
                task_check_point.is_successful = False
                task_check_point.save()

                assets = Asset.objects.filter(is_written_off=False)

                for asset in assets:
                    acquisition_date = asset.acquisition_date
                    months_passed = (current_date.year - acquisition_date.year) * 12 + (
                        current_date.month - acquisition_date.month)
                    depreciation_per_month = asset.cost / (asset.service_life * 12)
                    remaining_cost = asset.cost - (depreciation_per_month * months_passed)
                    asset.current_cost = Decimal(remaining_cost)
                    asset.last_recalculation_date = current_date
                    asset.save()

                task_check_point.last_processed_date = current_date
                task_check_point.is_successful = True
                task_check_point.save()

            logger.info(f"Successful completion of recalculation of fixed assets...")

        except TaskCheckPoint.DoesNotExist:
            return TaskCheckPoint.DoesNotExist
