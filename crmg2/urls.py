from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('dang-ky/', views.register_view, name='register'),
    path('dang-nhap/', views.login_view, name='login'),
    path('dang-xuat/', views.logout_view, name='logout'),
path('profile/', views.profile, name='profile'),  # trang xem
    path('edit/', views.edit_profile, name='edit_profile'),  # trang sửa

    ]