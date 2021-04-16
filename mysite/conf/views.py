from django.contrib.auth import login, authenticate, logout, get_user
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Story


# These objects will need to be transformed into models later on
# but as of right now they work since no information is being saved
# to the database in regards to the story


class Clue:
    clue_num = 0
    clue_text = ''
    clue_img_url = ''



# global temp_story
# temp_story = Story()
######################################################################

#This view function is used when signup is called
def signup(request):
   #  If the method is requesting to input data than create form, check if valid and save its elements
   if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #return to home page if account
            return redirect('home')
   else:
       #else create an empty form
        form = UserCreationForm()
    #return the form to signup.html to handle if error
   return render(request, 'signup.html', {'form': form})

#This view function is used when signout is called
def signout(request):
    logout(request)
    #redirect to the login page after the user is logged out
    return redirect('login')

def index(request):
    return render(request, 'index.html', context={})

def new_story(request):

    # check if story exists already, if it does delete it and create a new one
    created = Story.objects.filter(user=get_user(request)).exists()
    if created == True:
        Story.objects.filter(user=get_user(request)).delete()


    # Create and Give the story the user's name and default title/synopsis vals
    temp_story = Story()
    temp_story.user = get_user(request)
    temp_story.title = ''
    temp_story.synopsis = ''
    temp_story.clue_amount = 0
    ######################################################################

    # save new story to DB
    temp_story.save()

    return HttpResponseRedirect(reverse('storyboard'))
   
def load_story(request):
    return HttpResponseRedirect(reverse('storyboard'))

def save_story(request):
    # check if request is POST method and save vals if so else return to storyboard
    if request.method == 'POST':
        #find story
        tempStory = Story(user=get_user(request))
        tempStory.synopsis = request.POST['synopsis']
        tempStory.title = request.POST['title']

        #check if the user has a story created and delete it if so
        created = Story.objects.filter(user=get_user(request)).exists()
        if created == True:
            Story.objects.filter(user=get_user(request)).delete()


        tempStory.save()

        return HttpResponseRedirect(reverse('storyboard'))
    else:
        return HttpResponseRedirect(reverse('storyboard'))

def storyboard(request):
    # query for a story with a matching user
    # created = Story.objects.filter(user=get_user(request)).exists()
    # story = Story.objects.filter(user=get_user(request))
    story, created = Story.objects.get_or_create(user=get_user(request))
    return render(request, 'Storyboard.html', context={'title': story.title, 'synopsis': story.synopsis})

def add_clue(request):

    if request.method == 'POST':

        # Accesses the temp story add inserts a blank clue to the end of the clue list that is not connected to any clue
        # while increasing the clue counter in the story
        global temp_story
        temp_story.title = request.POST['title']
        temp_story.synopsis = request.POST['synopsis']
        temp_story.clue_amount += 1
        temp_clue = Clue()
        temp_clue.clue_num = temp_story.clue_amount
        ######################################################################

        # Reads in the contents of existing clues in the storyboard and stores the content to the stories clues list
        for x in temp_story.clue_list:
            x.clue_text = request.POST['clue' + str(x.clue_num) + '_text']
            x.clue_img_url = request.POST['clue' + str(x.clue_num) + '_img_url']
        ######################################################################

        # Adds an empty clue to the end of the stories clue list
        temp_story.clue_list.append(temp_clue)
        ######################################################################

    return HttpResponseRedirect(reverse('storyboard'))

def remove_clue(request):

    if request.method == 'POST':

        global temp_story
        # Accesses the temp_story and set the title and synopsis variables
        temp_story.title = request.POST['title']
        temp_story.synopsis = request.POST['synopsis']

        marked = []

        # Loop through the Clues in the story setting all available data
        for x in temp_story.clue_list:
            x.clue_text = request.POST['clue' + str(x.clue_num) + '_text']
            x.clue_img_url = request.POST['clue' + str(x.clue_num) + '_img_url']

            # If the clue has been marked for removal add the clue number to the marked list
            if request.POST['clue' + str(x.clue_num) + '_remove'] == "Remove":
                marked.append(int(x.clue_num) - 1)

        # Loop through the marked list and remove the corresponding clue from Clue list in
        # temp_story
        for x in reversed(marked):
            temp_clue = temp_story.clue_list[x]
            temp_story.clue_list.remove(temp_clue)
            del temp_clue

            # Once the clue is removed lower the clue nums of all clues that came after
            # the removed clue
            for clue in reversed(temp_story.clue_list):

                if clue.clue_num > x:
                    clue.clue_num -= 1
                else:
                    break

            # Decrease the clue amount in the temp_story
            temp_story.clue_amount -= 1

    return HttpResponseRedirect(reverse('storyboard'))

def refresh_story(request):

    if request.method == 'POST':
        # Accesses the story add inserts a blank clue to the end of the clue list that is not connected to any clue
        # while increasing the clue counter in the story
        story = Story(user=get_user(request))

        story.title = request.POST['title']
        story.synopsis = request.POST['synopsis']
        ######################################################################

        # Reads in the contents of existing clues in the storyboard and stores the content to the stories clues list
        # for x in story.clue_list:
        #     x.clue_text = request.POST['clue' + str(x.clue_num) + '_text']
        #     x.clue_img_url = request.POST['clue' + str(x.clue_num) + '_img_url']
        ######################################################################

    return HttpResponseRedirect(reverse('storyboard'))

# allows user to go back to the Storyboard editor from the visually displayed clues page
def return_to_editor(request):
   return render(request, 'Storyboard.html', context={})

# allows user to access visual clues page
def display_clues(request):
    return render(request, 'display_clues.html', context={})


