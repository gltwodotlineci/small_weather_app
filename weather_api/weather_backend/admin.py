from django.contrib import admin
from weather_backend.models import CateogryBlog, BlogPost, Product, Price


admin.site.register(BlogPost)
admin.site.register(CateogryBlog)
admin.site.register(Product)
admin.site.register(Price)
