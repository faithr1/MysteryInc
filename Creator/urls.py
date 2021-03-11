from django.urls import path

from Creator import views

# connects the url paths with their respected functions leading to the
# actions being taken on a page(moving between pages)
urlpatterns = [
    path('<username>/storyboard', views.storyboard, name='storyboard')
]
