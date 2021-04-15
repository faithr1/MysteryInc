from django.db import models


class DB_Story(models.Model):
    # details = models.CharField(max_length=500)
    # photo = models.ImageField(upload_to='evidence')
    # parent_clue = models.CharField(max_length=100)
    title = models.CharField(max_length=20)
    synopsis = models.CharField(max_length=500)
    clue_amount = models.IntegerField()
    # Clues = 
    author =models.CharField(max_length=30)