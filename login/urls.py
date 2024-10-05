from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    # 로그인 페이지
    path('', views.login_view, name='index'),
    # 회원가입 페이지
    path('signup/', views.signup_view, name='signup'),
    # 로그아웃 페이지
    path('logout/', views.logout_view, name='logout')
]
