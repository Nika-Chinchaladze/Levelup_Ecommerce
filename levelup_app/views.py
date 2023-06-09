from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Sum, Count

from .forms import LoginForm, RegisterForm, UserImageForm, UserCreditCardForm, PurchasePtoductForm, AddNewProductForm, UpdateProductForm
from .models import Product, SavedProduct, UserCreditCard, PurchasedProduct, SoldProduct
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
        all_products = Product.objects.all()
        # fewest product
        fewest_product = all_products.order_by("quantity")
        fewest_product = fewest_product[0] if len(fewest_product) > 0 else None
        # most popular product
        most_popular_product = PurchasedProduct.objects.values("product").annotate(
            total_quantity=Sum("quantity")).all().order_by("-total_quantity")
        most_popular_product = most_popular_product[0] if len(
            most_popular_product) else None
        # sold product
        sold_product = SoldProduct.objects.filter(
            product_provider=request.user).all()
        # product average price
        product_avg_prices = PurchasedProduct.objects.values("product").annotate(
            avg_money=Sum("money_spent")/Sum("quantity")).all()
        # product profit price
        product_profit_prices = sold_product.values("product").annotate(
            profit_money=Sum("money_gained")/Sum("quantity")).all()
        context = {
            "user": request.user,
            "products": all_products.order_by("-quantity"),
            "product_avg_prices": product_avg_prices,
            "product_profit_prices": product_profit_prices,
            "fewest_product": fewest_product,
            "most_popular_product": most_popular_product
        }
        return render(request, "levelup_app/home.html", context)


class MyOwnProductView(View):
    def get(self, request):
        context = {
            "user": request.user,
            "own_products": Product.objects.filter(provider=request.user).all()
        }
        return render(request, "levelup_app/own.html", context)


class UpdateOwnProductView(View):
    def get(self, request, pk):
        context = {
            "form": UpdateProductForm(),
            "chosen_product": Product.objects.get(id=pk)
        }
        return render(request, "levelup_app/update.html", context)

    def post(self, request, pk):
        chosen_product = Product.objects.get(id=pk)
        form = UpdateProductForm(request.POST)
        if form.is_valid():
            chosen_product.price = form.cleaned_data["price"]
            chosen_product.quantity = form.cleaned_data["quantity"]
            chosen_product.save()
            return HttpResponseRedirect(reverse("own"))


class RemoveFromSaleView(View):
    def get(self, request, pk):
        chosen_product = Product.objects.get(id=pk)
        chosen_product.in_sale = False
        chosen_product.save()
        return HttpResponseRedirect(reverse("own"))


class AddIntoSaleView(View):
    def get(self, request, pk):
        chosen_product = Product.objects.get(id=pk)
        chosen_product.in_sale = True
        chosen_product.save()
        return HttpResponseRedirect(reverse("own"))


class AddNewProductView(View):
    def get(self, request):
        context = {
            "user": request.user,
            "form": AddNewProductForm()
        }
        return render(request, "levelup_app/add.html", context)

    def post(self, request):
        form = AddNewProductForm(request.POST, request.FILES)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.provider = request.user
            form_instance.save()
            return HttpResponseRedirect(reverse("home"))


class CreditCardView(View):
    def get(self, request):
        context = {
            "user": request.user,
            "form": UserCreditCardForm(),
            "card": UserCreditCard.objects.filter(user=request.user).first()
        }
        return render(request, "levelup_app/credit.html", context)

    def post(self, request):
        form = UserCreditCardForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.user = request.user
            form_instance.save()
            return HttpResponseRedirect(reverse("credit-card"))


class UpdateProfileImageView(View):
    def get(self, request):
        context = {
            "form": UserImageForm()
        }
        return render(request, "levelup_app/image.html", context)

    def post(self, request):
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.user = request.user
            form_instance.save()
            return HttpResponseRedirect(reverse("home"))


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


class SavedProductView(View):
    def get(self, request):
        context = {
            "user": request.user,
            "saved_products": SavedProduct.objects.filter(user=request.user).all()
        }
        return render(request, "levelup_app/saved.html", context)


class SaveIntoCartView(View):
    def get(self, request, pk):
        chosen_product = Product.objects.get(id=pk)
        check_product = SavedProduct.objects.filter(
            product=chosen_product, user=request.user).first()
        if check_product is None:
            saved_product = SavedProduct(
                product=Product.objects.get(id=pk),
                user=request.user
            )
            saved_product.save()
        return HttpResponseRedirect(reverse("saved"))


class RemoveFromCartView(View):
    def get(self, request, pk):
        saved_product = SavedProduct.objects.get(id=pk)
        saved_product.delete()
        return HttpResponseRedirect(reverse("saved"))


class OrderProductView(View):
    def get(self, request, pk):
        context = {
            "user": request.user,
            "product": Product.objects.get(id=pk),
            "form": PurchasePtoductForm()
        }
        return render(request, "levelup_app/order.html", context)

    def post(self, request, pk):
        form = PurchasePtoductForm(request.POST)
        if form.is_valid():
            bougth_product = Product.objects.get(id=pk)
            customer_user = User.objects.get(id=request.user.id)
            # save purchased product into PurchasedProduct Model
            form_instance = form.save(commit=False)
            form_instance.user = customer_user
            form_instance.product = bougth_product
            form_instance.money_spent = request.POST["hidden_total_price"]
            form_instance.save()
            # decrease products total quantity
            bougth_product.quantity -= int(form.cleaned_data["quantity"])
            bougth_product.save()
            # decrease customer's balance on mastercard
            customer_money = customer_user.usercreditcard.creditcardmoney
            customer_money.money -= float(request.POST["hidden_total_price"])
            customer_money.save()
            # increase provide's balance on mastercard
            provider_user = bougth_product.provider
            provider_money = provider_user.usercreditcard.creditcardmoney
            provider_money.money += float(request.POST["hidden_total_price"])
            provider_money.save()
            # add product into SoldProduct model
            sold_product = SoldProduct(
                product=bougth_product,
                product_provider=provider_user,
                quantity=int(form.cleaned_data["quantity"]),
                money_gained=float(request.POST["hidden_total_price"])
            )
            sold_product.save()
            return HttpResponseRedirect(reverse("home"))
        else:
            context = {
                "user": request.user,
                "product": Product.objects.get(id=pk),
                "form": PurchasePtoductForm()
            }
            return render(request, "levelup_app/order.html", context)


class PurchasedProductsView(View):
    def get(self, request):
        context = {
            "user": request.user,
            "products": PurchasedProduct.objects.filter(user=request.user).all()
        }
        return render(request, "levelup_app/purchased.html", context)


class SoldProductView(View):
    def get(self, request):
        context = {
            "user": request.user,
            "sold_products": SoldProduct.objects.filter(product_provider=request.user).all()
        }
        return render(request, "levelup_app/sold.html", context)
