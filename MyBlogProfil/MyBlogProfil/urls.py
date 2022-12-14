"""MyBlogProfil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from article.views import article_list

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("article/",include('article.urls',namespace='article')),
    path('article/', include('article.urls', namespace='article')),
    
]

"""
path is Django routing syntax:
    the parameter article/ assigns the access path of the app
    include Distribute the path to the next processing
    namespace it is guaranteed to find a unique url, even if different apps
an article can have multiple pages, such a a list page, a detail page, etc, then the following two urls are required:
localhost/article/list/
localhost/article*/detail

"""