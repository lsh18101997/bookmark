from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id','title','modify_dt', 'create_dt', 'slug')
    list_filter=('modify_dt', )
    search_fields=('title', 'slug')
    prepopulated_fields={"slug":("title",)}
# Register your models here.

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())
