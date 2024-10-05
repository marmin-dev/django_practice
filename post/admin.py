from django.contrib import admin

from login.models import CustomUser
from post.models import Post

# Register your models here.
admin.site.register(Post)
admin.site.register(CustomUser)