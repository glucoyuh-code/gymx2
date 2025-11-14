from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Customer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Group, User
def home_view(request):
    """Render trang chủ sử dụng home.html."""
    return render(request, 'home.html')

# --- CHỨC NĂNG XÁC THỰC NGƯỜI DÙNG ---
def register_view(request):
    """Xử lý đăng ký người dùng mới. Gán vào nhóm 'Khách hàng'."""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            try:
                customer_group = Group.objects.get(name='Khách hàng')
                user.groups.add(customer_group)
            except Group.DoesNotExist:
                messages.warning(request, "Nhóm 'Khách hàng' chưa được thiết lập.")
            login(request, user)
            messages.success(request, 'Đăng ký thành công! Bạn đã được đăng nhập.')
            return redirect('home')
        else:
            messages.error(request, 'Đăng ký thất bại. Vui lòng kiểm tra lại thông tin.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    """Xử lý đăng nhập người dùng."""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Chào mừng {username}! Bạn đã đăng nhập thành công.')
                next_url = request.GET.get('next')
                return redirect(next_url or 'home')
            else:
                messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng.')
        else:
            messages.error(request, 'Đăng nhập thất bại. Vui lòng kiểm tra lại thông tin.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """Xử lý đăng xuất người dùng."""
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'Bạn đã đăng xuất thành công.')
    return redirect('home')


@login_required
def profile(request):
    profile, created = Customer.objects.get_or_create(user=request.user)
    # Đổi khóa từ 'user' thành 'profile'
    return render(request, 'accounts/profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    profile, created = Customer.objects.get_or_create(user=request.user)
    # Giữ nguyên việc truyền 'profile'

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/edit-profile.html', {'form': form, 'profile': profile})