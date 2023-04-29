from django.urls import path
from . import views


urlpatterns = [
    path("", views.AllProductView.as_view(), name="all"),
    path("login", views.LoginView.as_view(), name="login"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("home", views.HomeView.as_view(), name="home"),
    path("update-image", views.UpdateProfileImageView.as_view(), name="update-image"),
    path("detail/<int:pk>", views.ProductDetailView.as_view(), name="detail"),
    path("saved", views.SavedProductView.as_view(), name="saved"),
    path("save-in-cart/<int:pk>",
         views.SaveIntoCartView.as_view(), name="save-in-cart"),
    path("remove-from-cart/<int:pk>",
         views.RemoveFromCartView.as_view(), name="remove-from-cart")
]
