from django.shortcuts import render
from django.views import generic
import json
from datetime import datetime, date, timedelta
from django.http import HttpResponse
from WorkScheder.models import WorkSchedule
from django.contrib.auth.mixins import LoginRequiredMixin
import pdb

SERVICE_DOMAIN = 'localhost:8000'

def get_workSched(d):
    workPattern = "夜明休休夜明休休夜明日日夜明日休夜明休休夜明日日夜明休日"
    MAGIC_NUBER = 3
    index       = (d - date(1970, 1, 1)).days + 1
    return workPattern[(index + MAGIC_NUBER) % len(workPattern)]

def save_workSched(worksched, uid):
    workKind = '夜明日休ネ出'
    for dt, ws in worksched.items():
        if not ws in workKind:
            continue
        dt         = datetime.strptime(dt, '%Y-%m-%d').date()
        is_changed = not (get_workSched(dt) == ws)
        resistered = WorkSchedule.objects.filter(date=dt, user_id=uid)
        if resistered:
            resistered = resistered.get(date=dt)
            if is_changed:
                #WorkSchedule.objects.update()
                resistered.work_schedule = ws
                resistered.save()
            else:
                resistered.delete()
        else:
            if is_changed:
                #WorkSchedule(date=dt, work_schedule=ws).save()
                WorkSchedule.objects.create(date=dt, work_schedule=ws, user_id=uid)

def get_monthlyWorkSched(year, month, uid):
    start      = date(year, month, 1)
    end        = date(year, month+1, 1)
    changed_ws = \
        WorkSchedule.objects.filter(date__gte=start, date__lt=end, user_id=uid)
    monthly_ws = []
    for i in range(1, lastDay(year, month)+1):
        dt = date(year, month, i)
        try:
            ws = changed_ws.get(date=dt).work_schedule
        except WorkSchedule.DoesNotExist:
            ws = get_workSched(dt)
        monthly_ws.append({ 'sched':ws, 'date':str(dt) })
    return monthly_ws

def lastDay(year, month):
    return (date(year, month+1, 1) - timedelta(days=1)).day

# Create your views here.

class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'index.html'

    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(*args, **kwargs)
        return super(IndexView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #today                = date.today()
        #ws                   = get_monthlyWorkSched(today.year, today.month)
        #context['workSched'] = json.dumps(ws)
        context['domain']    = SERVICE_DOMAIN
        return context

    #def post(self, request, *args, **kwargs):
    def put(self, *args, **kwargs):
        if 'changes' in self.request.POST:
            uid     = self.request.user.id
            changes = json.loads(self.request.POST['changes'])
            save_workSched(changes, uid)
        return super().get(self.request, *args, **kwargs)

class ApiView(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):
        uid   = self.request.user.id
        year  = self.kwargs.get('year')
        month = self.kwargs.get('month')
        ws    = get_monthlyWorkSched(year, month, uid)
        return HttpResponse(json.dumps(ws))

