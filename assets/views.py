from django.http import JsonResponse
from assets.api.views.tasks import AssetRecalculator


def recalculate_assets_view(request):
    recalculator = AssetRecalculator()
    recalculator.recalculate_assets()
    data = {
        'message': 'Assets recalculation is complete...'
    }
    return JsonResponse(data)
