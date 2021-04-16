from django.db import models
import json

# create a custom manager to create story
# class StoryManager(models.Manager):
#     def create_story(self, user):
#         story = self.create(user=user)
#         return story


class Story(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.CharField(max_length=500)
    num_clues = models.IntegerField(null=True)
    user = models.CharField(max_length=100)

    # def save(self):
    #     super(Story, self).save()
