from django.db import models


class Homer(models.Model):
    homer_picture = models.ImageField(upload_to='homerpictures/')
    homer_mood = models.CharField(max_length=200)

    #def __str__(self):
        #return self.pk
