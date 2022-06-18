
from django.urls import path,include
from .views import view_hobby,add_hobby

app_name = "hobby"
urlpatterns = [
   
   path('',view_hobby,name="view_hobby_url"),
   path('add_hobby/', add_hobby, name="add_hobby_url")
   
]