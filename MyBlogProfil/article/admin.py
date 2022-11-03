from django.contrib import admin
from .models import ArticlePost

# Register your models here.

admin.site.register(ArticlePost)


"""
Website background concept : 
    Website backend, sometimes called website management backend, refers to a series of operations used to manage a website, such as adding, 
    and updating, and deleting data, in the early stage of project developement
    because there is no real user data and a complete test environement, the backgroun is frequently used to modify the test data,
    django has a built in good background used to modify the test data,
    django has a built-in good background managemen
"""

