from django.http import HttpResponse
from assets.tasks import AssetRecalculator


def recalculate_assets_view(request):
    recalculator = AssetRecalculator()
    recalculator.recalculate_assets()
    return HttpResponse('Assets recalculation is complete')
