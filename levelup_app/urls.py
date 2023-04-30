from django.urls import path
from . import views


urlpatterns = [
    path("", views.AllProductView.as_view(), name="all"),
    path("login", views.LoginView.as_view(), name="login"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("home", views.HomeView.as_view(), name="home"),
    path("update-image", views.UpdateProfileImageView.as_view(), name="update-image"),
    path("credit-card", views.CreditCardView.as_view(), name="credit-card"),
    path("detail/<int:pk>", views.ProductDetailView.as_view(), name="detail"),
    path("saved", views.SavedProductView.as_view(), name="saved"),
    path("purchased", views.PurchasedProductsView.as_view(), name="purchased"),
    path("save-in-cart/<int:pk>",
         views.SaveIntoCartView.as_view(), name="save-in-cart"),
    path("remove-from-cart/<int:pk>",
         views.RemoveFromCartView.as_view(), name="remove-from-cart"),
    path("order/<int:pk>", views.OrderProductView.as_view(), name="order")
]
