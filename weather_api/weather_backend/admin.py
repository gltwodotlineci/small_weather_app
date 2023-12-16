from django.contrib import admin
from weather_backend.models import CateogryBlog, BlogPost


admin.site.register(BlogPost)
admin.site.register(CateogryBlog)
