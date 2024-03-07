from django.http import HttpResponse, JsonResponse
from assets.api.views_tasks import AssetRecalculator


def recalculate_assets_view(request):
    recalculator = AssetRecalculator()
    recalculator.recalculate_assets()
    data = {
        'message': 'Assets recalculation is complete...'
    }
    return JsonResponse(data)
