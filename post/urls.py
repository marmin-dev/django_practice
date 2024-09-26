from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    # 메인 페이지
    path('', views.index, name='index'),
#     # 상세 페이지
    path('<int:post_id>/', views.detail, name='detail'),
#     # 수정 페이지
#     path('update/<int:post_id>/', views.update, name='update'),
#     # 새 게시글 페이지
    path('create/', views.create_post, name='create')
]
