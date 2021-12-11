from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from django.urls import reverse_lazy
from blog.models import Blog,Comments
from blog.forms import User_login,Normal,Image,Video,audio,documents,Com
# Create your views here.
def homeblog(request):
    model = Blog.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user:
            login(request,user)
    return render(request,'sim/home.html',{'model':model})

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
    return render(request,'sim/signin.html',context)

@login_required
def out(request):
    logout(request)
    return redirect('homeblog')

@login_required
def normalblog(request,pk):
    form = Normal
    norm = True
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = Normal(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = user
            f.save()
            return redirect('homeblog')
    context = {'form':form,'norm':norm}
    return render(request,'sim/upload.html',context)

@login_required
def imgblog(request,pk):
    form = Image
    img = True
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = Image(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = user
            f.save()
            return redirect('homeblog')
    context = {'form':form,'img':img}
    return render(request,'sim/upload.html',context)

@login_required
def vidblog(request,pk):
    form = Video
    vid = True
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = Video(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = user
            f.save()
            return redirect('homeblog')
    context = {'form':form,'vid':vid}
    return render(request,'sim/upload.html',context)

@login_required
def audblog(request,pk):
    form = audio
    aud = True
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = audio(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = user
            f.save()
            return redirect('homeblog')
    context = {'form':form,'aud':aud}
    return render(request,'sim/upload.html',context)

@login_required
def Docblog(request,pk):
    form = documents
    doc = True
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = documents(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = user
            f.save()
            return redirect('homeblog')
    context = {'form':form,'doc':doc}
    return render(request,'sim/upload.html',context)

class Detail(LoginRequiredMixin,DetailView):
    model = Blog
    template_name = 'sim/detail.html'

@login_required
def createcomment(request,pk,opk):
    user = get_object_or_404(User, pk=pk)
    blog = get_object_or_404(Blog, pk=opk)
    form = Com
    if request.method == "POST":
        form = Com(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = user
            f.blog = blog
            f.save()
            return redirect('homeblog')
    context = {'form':form}
    return render(request,'sim/postcomment.html',context)

class Commentupdate(LoginRequiredMixin,UpdateView):
    model = Comments
    fields = ['comment']
    template_name = 'sim/editcomment.html'

class Commentdelete(LoginRequiredMixin,DeleteView):
    model = Comments
    template_name = 'sim/deletecomment.html'
    success_url = reverse_lazy('homeblog')

class Postupdate(LoginRequiredMixin,UpdateView):
    model = Blog
    fields = ['title','post']
    template_name = 'sim/editpost.html'

class Postdelete(LoginRequiredMixin,DeleteView):
    model = Blog
    template_name = 'sim/deletepost.html'
    success_url = reverse_lazy('homeblog')
