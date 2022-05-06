from django.shortcuts import render, redirect
from .forms import registerview, loginview, changepass,passreset,setresetpass
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as auth_login


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


#
#
# def get_form_kwargs(self):
#     kwargs = super().get_form_kwargs()
#     kwargs['user'] = self.user
#     return kwargs


# forntend side views

def home(request):
    return render(request, "home.html")















#
# def password_reset_request(request):
# 	if request.method == "POST":
# 		form = passreset(request.POST)
# 		if form.is_valid():
# 			data = passreset.cleaned_data['email']
# 			associated_users = User.objects.filter(Q(email=data))
# 			if associated_users.exists():
# 				for user in associated_users:
# 					subject = "Password Reset Requested"
# 					email_template_name = "password_reset.txt"
# 					email = render_to_string(email_template_name)
# 					try:
# 						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
# 					except BadHeaderError:
# 						return HttpResponse('Invalid header found.')
# 					return redirect ("/password_reset/done/")
# 	password_reset_form = PasswordResetForm()
# 	return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form":password_reset_form})
#
