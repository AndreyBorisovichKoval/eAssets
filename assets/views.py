from django.http import JsonResponse


def ping(request):
    data = {'message': 'Server is up and running...'}
    return JsonResponse(data)


# def ping(request):
#     data = {'message': 'Server is up and running'}
#     return JsonResponse(data)
#     return HttpResponse("Server is up and running")
