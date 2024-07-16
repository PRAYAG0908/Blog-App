from django.contrib import admin
from .models import Tag, Author, Post, Comment

# Register your models here. username = Prayag password = Prayag2003
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    list_display = ("title","author",)
    list_filter = ("date","tags",)


admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)