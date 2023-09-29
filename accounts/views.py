from django.shortcuts import render,redirect
from django.views import View
from django.urls  import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from accounts.forms import SignUpForm,LoginForm



# Create your views here.
class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"account/login.html")
    
    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            print("ccccccccccccccccccccccccccccccccccc",form.cleaned_data)
            user = authenticate(
                request,
                username=request.POST.get("username"),
                password=form.cleaned_data.get("password")
            )
            if user:
                login(request,user)
                return redirect(reverse("post-list"))
            return render(
                request,'account/login.html',{"errors":"Usere Does not exist."}
                )
        return render(request,"account/login.html",{"errors": form.errors })
    
class SignUpView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"account/signup.html")
    
    def post(self,request,*args,**kwargs):
        data = request.POST
        print("data",data   )
        form = SignUpForm(request.POST  )
        if form.is_valid():
            user=User()
            user.username =data.get('username')
            user.set_password(data.get('password'))
            user.save()
            return redirect(reverse("login"))
        else:
            print("Error", form.errors)
            return render(
                request,"account/signup.html",{'errors': form.errors}
            )
        
class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect(reverse('login'))