from django.db import models

from login.models import CustomUser


# 게시글 모델
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    # author = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, related_name="user", on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_content = models.CharField(max_length=600)
    comment_user = models.ForeignKey(CustomUser, related_name="comment_user", on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, related_name="post", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_id

    class Meta:
        db_table = 'comment'