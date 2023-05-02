from django.urls import path
from . import views


urlpatterns = [
    path("", views.AllProductView.as_view(), name="all"),
    path("login", views.LoginView.as_view(), name="login"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("home", views.HomeView.as_view(), name="home"),
    path("own", views.MyOwnProductView.as_view(), name="own"),
    path("remove-from-sale/<int:pk>", views.RemoveFromSaleView.as_view(),
         name="remove-from-sale"),
    path("add-into-sale/<int:pk>",
         views.AddIntoSaleView.as_view(), name="add-into-sale"),
    path("add", views.AddNewProductView.as_view(), name="add"),
    path("update-image", views.UpdateProfileImageView.as_view(), name="update-image"),
    path("credit-card", views.CreditCardView.as_view(), name="credit-card"),
    path("detail/<int:pk>", views.ProductDetailView.as_view(), name="detail"),
    path("saved", views.SavedProductView.as_view(), name="saved"),
    path("purchased", views.PurchasedProductsView.as_view(), name="purchased"),
    path("sold", views.SoldProductView.as_view(), name="sold"),
    path("save-in-cart/<int:pk>",
         views.SaveIntoCartView.as_view(), name="save-in-cart"),
    path("remove-from-cart/<int:pk>",
         views.RemoveFromCartView.as_view(), name="remove-from-cart"),
    path("order/<int:pk>", views.OrderProductView.as_view(), name="order"),
    path("update/<int:pk>", views.UpdateOwnProductView.as_view(), name="update")
]
