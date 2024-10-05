from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from login.forms import LoginForm, CustomUserCreationForm


# 로그인
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # 유효한 사용자 객체를 로그인에 사용
                return redirect("post:index")
    else:
        form = LoginForm()
    return render(request, 'login/index.html', {'form': form})

# 회원 가입
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post:index')
    else:
        form = CustomUserCreationForm()

    return render(request, 'login/signup.html', {'form': form})

# 로그아웃
def logout_view(reqeust):
    logout(reqeust)
    return redirect("login:index")