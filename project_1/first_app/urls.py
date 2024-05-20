from django.urls import path
from . import views
# from views import contact

urlpatterns = [
  
    path("courses/",views.courses),
    path("about/",views.about),
    path("",views.home),
    
]
