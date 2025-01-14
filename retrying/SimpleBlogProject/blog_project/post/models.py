from django.db import models
from categories.models import Category
from author.models import Author


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category= models.ManyToManyField(Category)
    # ekta post multiple category er moddhe thakte pare abar ekta category multiple post er moddhe thakte pare 
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    # many to one relation er jonno 
    # on_delete=models.CASCADE author delete hole tar post oo delete hoiya jabe  
    
    def __str__(self):
        return self.title