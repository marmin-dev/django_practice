from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('login/', include('login.urls'))
]
