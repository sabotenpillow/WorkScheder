from django.shortcuts import render
from django.views import generic
import json
from datetime import date, timedelta

def get_workSched(d):
    workPattern = "夜明日休夜明休休夜明休休夜明日日夜明休日夜明休休夜明日日"
    MAGIC_NUBER = 3
    index       = (d - date(1970, 1, 1)).days + 1
    return workPattern[(index + MAGIC_NUBER) % len(workPattern)]
    #workSched = [
    #    {
    #        'title': 'ppo',
    #        'start': '2020-03-02'
    #    },
    #    {
    #        'title': 'tenshi',
    #        'start': '2020-03-02'
    #    }
    #]
    #return workSched

def get_monthlyWorkSched():
    today = date.today()
    mWorkSched = []
    for i in range(1, lastDay(today.year, today.month)+1):
        d = date(today.year, today.month, i)
        mWorkSched.append({ 'sched':get_workSched(d), 'date':str(d) })
    return mWorkSched

def lastDay(year, month):
    return (date(year, month+1, 1) - timedelta(days=1)).day

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['test'] = ['mama', 'mimi']
        context['workSched'] = json.dumps(get_monthlyWorkSched())
        return context
