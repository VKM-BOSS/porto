from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from cloud_storage.models import storage
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from cloud_storage.forms import User_login,Image_form,Video_form,Audio_form,Document_form
# Create your views here.
def homecloud(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user:
            login(request,user)
    return render(request,'Home.html')

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
    return render(request,'signin.html',context)

@login_required
def out(request):
    logout(request)
    return redirect('home')

@login_required
def image_upload(request,pk):
    form = Image_form
    img = True
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = Image_form(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = user
            f.save()
            return redirect('home')
    context = {'form':form,'img':img}
    return render(request,'upload.html',context)

@login_required
def video_upload(request,pk):
    form = Video_form
    vid = True
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = Video_form(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = user
            f.save()
            return redirect('home')
    context = {'form':form,'vid':vid}
    return render(request,'upload.html',context)

@login_required
def audio_upload(request,pk):
    form = Audio_form
    aud = True
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = Audio_form(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = user
            f.save()
            return redirect('home')
    context = {'form':form,'aud':aud}
    return render(request,'upload.html',context)

@login_required
def document_upload(request,pk):
    form = Document_form
    doc = True
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = Document_form(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = user
            f.save()
            return redirect('home')
    context = {'form':form,'doc':doc}
    return render(request,'upload.html',context)

class DetailImage(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Image'] = True
        return context

class DetailVideo(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Video'] = True
        return context

class DetailAudio(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Audio'] = True
        return context

class DetailDocument(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Document'] = True
        return context

class Detailinter(LoginRequiredMixin,DetailView):
    model = storage
    template_name = 'detailinter.html'

class Deletefile(LoginRequiredMixin,DeleteView):
    model = storage
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
