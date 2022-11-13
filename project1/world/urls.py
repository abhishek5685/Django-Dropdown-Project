from django.urls import path
from world import views
urlpatterns = [
    path('home/',views.home,name="home"),
    path('state_list/',views.state_data,name="state_data"),

]
