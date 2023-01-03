from django.urls import path
from . import views

urlpatterns = [
    # path('city/', views.get_city, name='city'),  #the path for our get_city view
    # path('', views.index,name='post'),  #the path for our index view
    # path('submit/', views.postdata, name = 'post-data'),
    path('city/',views.CityApi.as_view()),
    path('addcity/', views.addcity, name = 'addcity')
]