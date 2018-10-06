from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('',views.allblogs, name = 'allblogs'),
    path('<int:blog_id>/', views.detail, name= "detail"),
    #look for an integer that is after blog/, and assign the name "blog_id" to it
]
