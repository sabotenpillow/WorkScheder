from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from modules.mixins import MyselfOnlyMixin
## import utils
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import imgkit, io
from PIL import Image
import json
## import models
from WorkScheder.models import WorkSchedule
from accounts.models import WorkPatterns, User
from accounts.forms import UserUpdateForm, UserWorkPatternUpdateForm
## debug
import pdb

SERVICE_DOMAIN = 'localhost:8000'

def get_workSched(d, user):
    #workPattern = "夜明休休夜明休休夜明日日夜明日休夜明休休夜明日日夜明休日"
    #MAGIC_NUBER = 3
    pattern = user.workPattern.pattern
    adj_num = user.adjust_num
    index       = (d - date(2000, 1, 1)).days
    return pattern[(index + adj_num ) % len(pattern)]

def save_workSched(worksched, user):
    workKind = '夜明日休ネ出'
    for dt, ws in worksched.items():
        if not ws in workKind:
            continue
        dt         = datetime.strptime(dt, '%Y-%m-%d').date()
        is_changed = not (get_workSched(dt, user) == ws)
        resistered = WorkSchedule.objects.filter(date=dt, user_id=user.id)
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
                WorkSchedule.objects.create(date=dt, work_schedule=ws, user_id=user.id)

def get_monthlyWorkSched(year, month, user):
    start      = date(year, month, 1)
    #end        = date(year, month+1, 1)
    end        = start + relativedelta(months=1)
    changed_ws = \
        WorkSchedule.objects.filter(date__gte=start, date__lt=end, user_id=user.id)
    monthly_ws = []
    for i in range(1, lastDay(year, month)+1):
        dt = date(year, month, i)
        try:
            ws = changed_ws.get(date=dt).work_schedule
            changed_flag = True
        except WorkSchedule.DoesNotExist:
            ws = get_workSched(dt, user)
            changed_flag = False
        monthly_ws.append({ 'sched':ws, 'date':str(dt), 'changed':changed_flag })
    return monthly_ws

def lastDay(year, month):
    #return (date(year, month+1, 1) - timedelta(days=1)).day
    return (date(year, month, 1) + relativedelta(months=1,days=-1 )).day

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
            user    = self.request.user
            changes = json.loads(self.request.POST['changes'])
            save_workSched(changes, user)
        return super().get(self.request, *args, **kwargs)

class SetPatternView(MyselfOnlyMixin, generic.UpdateView):
    template_name = 'update.html'
    model         = User
    form_class    = UserWorkPatternUpdateForm
    success_url   = reverse_lazy('worksched:index')

class ApiView(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):
        user  = self.request.user
        if user.workPattern is None:
            return HttpResponse(json.dumps([]))
        year  = self.kwargs.get('year')
        month = self.kwargs.get('month')
        ws    = get_monthlyWorkSched(year, month, user)
        return HttpResponse(json.dumps(ws))

class getSchedWithImageView(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):
        ##---- prepare for accessing to Web page
        host = request.get_host()
        path = str(reverse_lazy('worksched:index'))
        url = 'http://' + host + path
        cookies = request.COOKIES
        options = {
            'xvfb': '',
            'cookie': [
                ('csrftoken', cookies['csrftoken']),
                ('sessionid', cookies['sessionid']),
            ],
        }

        ##---- access to Web page
        img = None
        try:
            img = imgkit.from_url(url, False, options=options)
            #img = imgkit.from_string('Success', False, options=options)
        except:
            img = imgkit.from_string('Error', False, options=options)

        #pdb.set_trace()
        img_io = io.BytesIO(img)
        img_pil = Image.open(img_io)

        ## generate HttpResponse
        #response = HttpResponse(image, content_type='image/jpeg')
        response = HttpResponse(content_type='image/jpeg')
        img_pil.save(response, 'jpeg')
        return response
