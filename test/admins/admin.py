from django.contrib import admin

# Register your models here.

from .models import Post, Member, dosen
admin.site.register(Post)
admin.site.register(Member)
admin.site.register(dosen)
