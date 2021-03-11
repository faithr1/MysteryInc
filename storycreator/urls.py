from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('new_story/',views.new_story,name="new_story"),
    path('load_story/',views.load_story,name="load_story")
]