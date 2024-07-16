from django.contrib import admin
from app.models import *
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display=('user', 'bio')
admin.site.register(Profile,ProfileAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display=('title','author', 'status')
admin.site.register(Post,PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
admin.site.register(Category, CategoryAdmin)

admin.site.register(BlogImages)