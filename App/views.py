from django.shortcuts import render, redirect
from .forms import registerview, loginview, changepass, passreset, setresetpass, todoform
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as auth_login
from .models import Todo


# Create your views here.


# authentication  views


def register(request):
    form = registerview()
    if request.method == "POST":
        email = request.POST["email"]
        form = registerview(request.POST)
        if form.is_valid():
            form.save()
            subject = "testing mail"
            message = "thank you for  the regitration"
            email_from = settings.EMAIL_HOST_USER
            reciver_list = [email, ]
            send_mail(subject, message, email_from, reciver_list)
            return redirect('login')
    else:
        form = registerview()
    con = {"form": form}
    return render(request, "register.html", con)


def login(request):
    form = loginview()
    if request.method == "POST":
        uname = request.POST["username"]
        upass = request.POST["password"]
        user = authenticate(username=uname, password=upass)
        # print(user, "sssssssssssssssssssssssssssssssssssssssssssssssssssssssss")

        if user is not None:
            login(request, user)
            messages.success(request, "please enter correct user")
            return redirect("/index/")
        else:
            messages.error(request, "please enter correct user")

            return redirect("/login/")
    else:
        if request.user.is_authenticated:
            return redirect("/home/")
        else:
            pass
    con = {'form': form}

    return render(request, "login.html", con)


def logout(request):
    django_logout(request)
    return redirect("/login/")


def ChangePassView(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = changepass(request.user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your Password change Successfully")
                return redirect("/home/")
        else:
            form = changepass(request.user)
        con = {'form': form}
        return render(request, "changepassword.html", con)
    else:
        messages.info(request, "please login first")

    return render(request, "changepassword.html")


# forntend side views

def home(request):
    if request.method == 'POST':

        form = todoform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "saved sussessfully")
            return redirect("home")
        else:
            form = todoform(request.POST)
            return redirect("home")

    else:
     form = todoform(request.POST)
    data = Todo.objects.all()
    con = {"form": form,"data":data}
    return render(request, "home.html", con)

def update(request,id):
    data = Todo.objects.all()
    getdata=Todo.objects.get(id=id)
    if request.method=="POST":
        form = todoform(request.POST,instance=getdata)
        if form.is_valid():
            form.save()
            messages.success(request,"update successfully")
            return redirect("home")
        else:
            form =todoform(instance=getdata)
    else:
        form = todoform(instance=getdata)
    con={"data":data,"form":form}
    return render(request,"home.html",con)

def delete(request,id):
    data=Todo.objects.get(id=id)
    data.delete()
    return redirect("home")