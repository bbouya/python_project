from email.policy import default
from enum import _auto_null
from pyexpat import model
from sre_constants import MAX_UNTIL
from time import time
from django.db import models


""""
Introduction
Databases and Modeles
a database is a place for sorting electronic files, storing independent collections of data
a database consits of multiple data tables.
# By the default the database is the file db.sqlite3 you may want to switch to anther
database after site goes live, but we dont need to discuess that yet
operating the database uses complex sql statements, which is a completely different language from python
which is undoubtedly difficlt for me

"""


# Create your models here.

from django.contrib.auth.models import User 

from django.utils import timezone 

class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length = 100)

    body = models.TextField()

    created = models.DateTimeField(default= timezone.now)

    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.title

"""
Each model is represented as a django.db.models.Model subclass of the class from 
which it inherits all the methods needed to manipulate the database.
Each field is an instance of a Field class, for example character Fields are represented asss 
CharField, and datetime fields are represneted as DateTimeField.
This will tell django what type of data to handle.
Defining certain Field class instance requires parameters, for example CharField requires max_lenght
Use to Foreignkey defie a relationship, this will tell django that each (or more) articlePost object is associated with an user object.

"""

"""
ArticlePost the class defines the elements that an article must have author, title, body creation time, and update time,
we can also define some additional content, ArticlePost the behavior of the data in the specification

"""


"""
The inner class define hhow the data is arranged Meta, indicates that it
will be arrangent in reverse order of creation time, ensuring that the 
last article are always at the top of the page, Note that it is a tuple, don't 
forget the trailing comma when there is only on element in the parentheses, ordering -created ordering 
"""


