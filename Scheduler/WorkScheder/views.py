from django.shortcuts import render
from django.views import generic
import json
from datetime import date, timedelta
from django.http import HttpResponse

SERVICE_DOMAIN = 'localhost:8000'

def get_workSched(d):
    workPattern = "夜明日休夜明休休夜明休休夜明日日夜明休日夜明休休夜明日日"
    MAGIC_NUBER = 3
    index       = (d - date(1970, 1, 1)).days + 1
    return workPattern[(index + MAGIC_NUBER) % len(workPattern)]

def get_monthlyWorkSched(year, month):
    mWorkSched = []
    for i in range(1, lastDay(year, month)+1):
        d = date(year, month, i)
        mWorkSched.append({ 'sched':get_workSched(d), 'date':str(d) })
    return mWorkSched

def lastDay(year, month):
    return (date(year, month+1, 1) - timedelta(days=1)).day

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context              = super().get_context_data(**kwargs)
        today                = date.today()
        ws                   = get_monthlyWorkSched(today.year, today.month)
        context['domain']    = SERVICE_DOMAIN
        context['workSched'] = json.dumps(ws)
        return context

class ApiView(generic.View):
    def get(self, request, *args, **kwargs):
        year  = self.kwargs.get('year')
        month = self.kwargs.get('month')
        ws    = get_monthlyWorkSched(year, month)
        return HttpResponse(json.dumps(ws))

