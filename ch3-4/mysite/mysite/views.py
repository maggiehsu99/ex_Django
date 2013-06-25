__author__ = 'maggiehsu99'
from django.http import HttpResponse
import datetime



def hello(request):
    return HttpResponse("Hello world")

def my_homepage(request ):
    return HttpResponse("welcome to Django group")

def current_datetime(request):
    now=datetime.datetime.now()
    html="<head><body>now is %s </body> </head>"% now
    return  HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)