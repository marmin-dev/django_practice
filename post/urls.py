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
    path('create/', views.create_post, name='create'),
     #게시글 삭제
    path('delete/<int:post_id>/', views.delete_post, name="delete"),
    # 게시글 업데이트
    path('update/<int:post_id>/', views.update_post, name="update"),
    #  댓글 추가
    path('comment/<int:post_id>', views.create_comment, name="comment")
]
