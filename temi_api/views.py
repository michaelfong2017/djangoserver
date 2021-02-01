from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from temi_api.models import Credential


# Create your views here.
def current_datetime():
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now

    return HttpResponse(html)

@csrf_exempt
def post_credential(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.raw_post_data)
            print(data)
        except:
            print('nope')
        return HttpResponse('yo')
