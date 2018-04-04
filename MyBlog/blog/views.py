from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import ckeditorForm
from django.contrib.auth.models import User
# Create your views here.


@login_required
def sucessLogin(request):
    return render(request,'registration/sucessLogin.html',{})

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