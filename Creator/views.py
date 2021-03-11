from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import Http404

from Creator.models import User

# Variable that stores the logged in user
# may want to edit this so that it is more secure currently acts as a validation
# and is unable to be altered due to not being connected with the login page yet
selected = User.objects.get(pk='admin')


# Loads in the storyboard page allowing for an author to begin creating/editing
# their story
def storyboard(request, username):
    # First checks to see if the username exists in the database
    try:
        user = User.objects.get(pk=username)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    # Checks to see if the username corresponds to the logged in user
    # if it does then progress to the storyboard else alert user to
    # the error
    if user.username == selected.username:
        author_name = user.username
        context = {
            'author_name': author_name,
        }
        # may need to alter path once files are being merged in github
        return render(request, 'Creator/Storyboard.html', context)
    else:
        raise Http404("Username does not match logged in user")
