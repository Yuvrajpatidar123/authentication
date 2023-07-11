from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib import auth
from .models import Contactus

# Create your views here.
def index(request):
    return render(request,'index.html')
def index2(request):
    return render(request,'index2.html')
def signup(request):
    return render(request,'Signup.html')
def signin(request):
    return render(request,'Signin.html')
def contact(request):
    return render(request,'Contact.html')

def signuppage(request):

    if request.method=="POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        unm = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        try:
            user = User.objects.get(username = unm)
            return render(request,'Signup.html')
        except:
            user = User.objects.create_user(first_name = fname,last_name = lname, username = unm, email = email, password = pwd)
            user.save()
            return render(request,'Signin.html')
    else:
        return render(request, 'Signin.html')
def signinpage(request):
    if request.method =="POST":
        unm =request.POST['username']
        pwd =request.POST['password']

        user = auth.authenticate(username = unm, password = pwd) 
        if user is not None:
            auth.login(request,user)
            return redirect('userhome')
        else:
            return render(request,'Signup.html')
    else:
        return render(request, 'signin.html')
def userhome(request):
    
    return render(request,'userhome.html')
def logout(request):
    auth.logout(request)
    return render(request,'index2.html')

def contactuspage(request):

    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        desc = request.POST['desc']

        contact = Contactus(name = name,email = email, mobile = mobile, desc = desc)
        contact.save()
        return render(request,'index2.html')
    else:
        return render(request, 'Contact.html')

