from django.urls import path,include
from . import views

app_name = 'article'

urlpatterns = [
    #include the different patern in here

    path('article_list/', views.article_list, name='article_list'),
    
]
