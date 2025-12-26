from django.contrib import admin
from .models import Category, Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name')
    list_editable = ('is_featured',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'blog', 'comment', 'created_at')
    search_fields = ('comment', 'user__username', 'blog__title')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
