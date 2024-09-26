from django.shortcuts import render, get_object_or_404, redirect

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


# 게시글 등록 페이지
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        content = request.POST.get("content")
        post = Post(title=title, author=author, content=content)
        post.save()
        return redirect('post:detail', post_id=post.post_id)
    return render(request, 'post/create.html')
