from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from mybookmark.models import Bookmark
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class BookmarkLV(LoginRequiredMixin, ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

    def get_object(self):
        bookmark_id = self.kwargs['bookmark_id']
        bookmark = get_object_or_404(Bookmark, pk=bookmark_id)
        return bookmark
