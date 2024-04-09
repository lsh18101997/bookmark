from django.urls import path
from . import views

app_name = "mybookmark"

urlpatterns = [
    path("", views.BookmarkLV.as_view(), name="index"),
    path("<int:bookmark_id>/", views.BookmarkDV.as_view(), name="detail"),

]