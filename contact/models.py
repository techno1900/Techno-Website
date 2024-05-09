from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=500)
    description = models.TextField()
    is_replyed = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
    


    

