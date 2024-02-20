from django.http import HttpResponse
from assets.tasks import AssetRecalculator


def recalculate_assets_view(request):
    recalculator = AssetRecalculator()
    recalculator.recalculate_assets()
    # Дополнительный код, который выполняется после перерасчета активов
    return HttpResponse('Assets recalculation is complete')  # Пример возврата HTTP-ответа
