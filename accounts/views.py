from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import CustomUserForm
from django.contrib.auth import get_user_model,authenticate
from django.contrib.auth import login as log_in
from django.contrib.auth import logout as log_out
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.decorators import permission_required, login_required



# Create your views here.
@permission_required('accounts')
def list(request):
    return HttpResponse("리스트페이지 만들자")



@login_required
def detail(request):
    user = request.user
    return render(request,"accounts/detail.html",{"user":user})



@permission_required('accounts')
def create(request):
    if request.method=="POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movies:list")
    else:
        form = CustomUserForm()
    return render(request,"accounts/form.html",{"form":form})


@permission_required('accounts')
def delete(request):
    return HttpResponse("딜리트 페이지 만들자")

@login_required
def update(request):
    if request.method=="POST":
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("movies:list")   
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,"accounts/form.html",{"form":form})


@login_required    
def logout(request):
    log_out(request)
    return redirect("movies:list")
    
def login(request):
    if request.method=="POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                log_in(request,user)
                return redirect("movies:list")
    else:
        form = AuthenticationForm()
    return render(request,"accounts/form.html",{"form":form})