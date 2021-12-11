from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from mail.forms import User_login
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
from mail.models import sender
# Create your views here.
def homemail(request):
    model = sender.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user:
            login(request,user)
    return render(request,'faq\home.html',{'model':model})

@login_required
def out(request):
    logout(request)
    return redirect('mailhome')

def signup(request):
    form = User_login
    signedup = False
    if request.method == "POST":
        form2 = form(request.POST)
        if form2.is_valid():
            f = form2.save()
            f.set_password(f.password)
            f.save()
            signedup = True
    context = {'signup':True,'form':form,'signedup':signedup}
    return render(request,'faq\signin.html',context)

def senter(request,pk):
    sent = False
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        fm = request.POST['fm']
        tm = request.POST['tm']
        sub = request.POST['sub']
        cont = request.POST['ta']
        pas = request.POST['pass']
        email = EmailMessage()
        email['from'] = pk
        email['to'] = tm
        email['subject'] = sub
        email.set_content(cont)
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
          smtp.ehlo()
          smtp.starttls()
          smtp.login(fm,pas)
          smtp.send_message(email)
          s = sender.objects.get_or_create(user=user,fmail=fm,tmail=tm,subject=sub,content=cont)
          sent = True
    context={'sent':sent}
    return render(request,'faq\sender.html',context)
