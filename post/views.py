from django.shortcuts import render, get_object_or_404

from post.models import Post


# 게시글 목록 페이지
def index(request):
    post_list = Post.objects.all().order_by('-post_id')
    context = {'posts': post_list}
    return render(request, 'post/index.html', context)


# 게시글 상세 페이지
def detail(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    context = {'post': post}
    return render(request, 'post/detail.html', context)
