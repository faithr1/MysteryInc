from django.db import models


# Create your models here.

# Basic model for the user profile as a means of testing acquiring
# the username for new story creation and shall be replaced when merging
# all created documents together
class User(models.Model):
    # variables store the users username (author name) and password
    # variable sizes can be changed later once a determined length is
    # chosen
    username = models.CharField(max_length=100, default='username', primary_key=True)
    password = models.CharField(max_length=100, default='password')

    def __str__(self):
        return self.username


# Basic model for a story element storing the title for the story
# and the author of the story may want to use this for saving a given
# story to the database rather then loading the story from a text file
# stored on the users PC
class Story(models.Model):
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    story_title = models.CharField(max_length=100, default='')
    story_description = models.CharField(max_length=500, default='')


# Basic model for a clue element storing all its relative information
# and is linked to a story element thus allowing for multiple clues to
# be connected to any given story
class Clue(models.Model):
    story_title = models.ForeignKey(Story, on_delete=models.CASCADE)
    clue_text = models.TextField(default='')
    clue_img = models.TextField(default='')
