from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import ckeditorBlog
from .forms import ckeditorForm
from django.contrib.auth.models import User
# Create your views here.
import re

@login_required
def sucessLogin(request):
    return render(request,'registration/sucessLogin.html',{})

@login_required
def ckeForm(request):
    user1 = get_object_or_404(User,id=1)
    if request.method == 'POST':
        form = ckeditorForm(request.POST)
        if form.is_valid():
            cke = form.save(commit=False)
            cke.user = user1
            cke.save()
            return HttpResponse('sucess')
    else:
        form = ckeditorForm()
    return render(request,'registration/cke.html',{'form':form})

def test(request):
    blogs = ckeditorBlog.objects.filter(id=2)
    power = re.compile(
        r'<img alt="" src="/media/uploads/2018/04/04/u6489861613933641907fm27gp0_E6SKzcp.jpg" style="height:313px; width:500px" />', re.I)
    bs = ''
    for blog in blogs:
        # print(blog.content)
        bs = power.match(blog.content)
        print(bs)
    content = {'blogs':bs}
    return render(request,'registration/test.html',content)
