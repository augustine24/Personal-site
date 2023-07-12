
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.text import slugify
from .models import Post
from .models import SiteBackground
from .models import YourImageModel 

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)
        


admin.site.register(SiteBackground) 

admin.site.register(YourImageModel)

    