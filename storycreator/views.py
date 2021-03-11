from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):

    return render(request,'storycreator/index.html',context={})
def new_story(request):
    return render(request,'storycreator/new_story.html',context={})
def load_story(request):
    return render(request,'storycreator/load_story.html',context={})