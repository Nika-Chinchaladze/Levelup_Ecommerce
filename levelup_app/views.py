from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views import View

from .forms import LoginForm, RegisterForm
from .models import UserImage, Product
# Create your views here.


class LoginView(View):
    def get(self, request):
        context = {
            "form": LoginForm(),
            "user": request.user
        }
        return render(request, "levelup_app/login.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
            else:
                messages.error(
                    request, "User does not exist, please create account!")
                return HttpResponseRedirect(reverse("register"))
        else:
            context = {
                "form": form,
                "user": request.user
            }
            return render(request, "levelup_app/login.html", context)


class RegisterView(View):
    def get(self, request):
        context = {
            "form": RegisterForm(),
            "user": request.user
        }
        return render(request, "levelup_app/register.html", context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your Account has been created successfully, Please login in.")
            return HttpResponseRedirect(reverse("login"))
        else:
            context = {
                "form": form,
                "user": request.user
            }
            return render(request, "levelup_app/register.html", context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, "levelup_app/logout.html")


class HomeView(View):
    def get(self, request):
        context = {"user": request.user}
        return render(request, "levelup_app/home.html", context)


class AllProductView(View):
    def get(self, request):
        context = {
            "user": request.user,
            "products": Product.objects.all()
        }
        return render(request, "levelup_app/all.html", context)


class ProductDetailView(View):
    def get(self, request, pk):
        context = {
            "user": request.user,
            "product": Product.objects.get(id=pk)
        }
        return render(request, "levelup_app/detail.html", context)
