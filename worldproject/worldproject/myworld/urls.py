from django.urls import path
from . import views

app_name='myworld'
urlpatterns = [
   
    path('',views.index,name="index"),
    path('world/<int:world_id>/',views.details,name="details"),
    path('add/',views.add_world,name="add_world"),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name="delete"),
]