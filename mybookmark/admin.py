from django.contrib import admin
from mybookmark.models import Bookmark

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'url')

# admin.site.register(Bookmark)
