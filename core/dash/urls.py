from django.urls import path,include
from . import views 


urlpatterns = [
    path('',views.mainPage,name = "mainPage"),
    path('api/citydata', views.CityData.as_view()),
    path('api/genderdata',views.GenderAge.as_view())
]
