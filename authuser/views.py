from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from authuser.models import User
from django.contrib.auth import login,logout,authenticate


class LoginView(View):

    def get(self,request):
        if request.user.is_authenticated:
            messages.warning(request,'عفوا انت حاليا داخل النظام')
            return redirect('authuser:test_url')
         

        return render(request,'authuser/login.html')

    def post(self,request):

        if request.method =='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            next_url=request.POST.get('next')

            if username and password:
                user=authenticate(request,username=username,password=password)
                if user:
                    
                    if user.is_active:
                        user=authenticate(request,username=username,password=password)
                        login(request,user)
                        messages.success(request,'مبرروك تم الدخول للنظام بنجاح')
                        return redirect(next_url or '/' )
            
                    messages.error(request,'عفوا هذا المستخدم غير نشط')
                messages.error(request,'عفوا  هذا المستخدم غير موجود')

                
                
                
            messages.error(request,'عفوا  لابد من ادخال كلمة السر واسم المستخدم   ')

            

        return render(request,'authuser/login.html')
    
def logoutview(request):
    logout(request)
    messages.success(request,'تم اتلخروج من النظام بنجاح')
    return redirect('authuser:login')
    
def test_url(request):
    return render(request,'authuser/test_url.html',{})


