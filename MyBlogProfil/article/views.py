from django.shortcuts import render
from django.http import HttpResponse
from .models import ArticlePost

# Create your views here.

def article_list(request):
    articles = ArticlePost.objects.all()

    context = {"articles": articles}

    return render(request, 'article/list.html', context)



"""
The code is also very straightforward and the analysis as follows
    from .models import ArticlePost models.py import ArticlePost data classes from
    ArticlePost.objects.all() is a method of the data class that can get all the object (blog posts) and pass them to the articles variabel
    context defines the context that needs to be passed to the template, here articles,
    finally the render function is returned, its role is to combine the template and context and return the rendered HttpResponse object, 

render The variables are broken down as follows: 
    request is a fixed object, you can just write it.
    article/list.html defines the location and name of the template file
    Context defines the context that needs to be passed into the templates file
    
"""
