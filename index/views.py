from django.http import HttpResponse


def index_view(request):
    index_text = {"message": "Server is up and running..."}
    return HttpResponse(index_text['message'])
    # return HttpResponse("message': 'Server is up and running...")
