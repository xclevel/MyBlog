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
    blogs = ckeditorBlog.objects.filter(id=3)
    # 正则表达式需要重写，此处应急使用
    power = r'<img alt="" src="/\w+/\w+/\w+/\w+/\w+/\w+.jpg" style="\w+:\w+;\w+:\w+" />'
    rs = ''
    for blog in blogs:
        # print(blog.content)
        # bs = blog.content[3:123]
        print(blog.content)
        rs = re.findall(power,blog.content)
    content = {'blogs':rs}
    return render(request,'registration/test.html',content)































