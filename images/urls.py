from django.urls import path
from .views import image_create,imaage_detail,image_like,image_list

app_name = 'images'
urlpatterns = [
    path('create/',image_create,name='create'),
    path('list/',image_list,name='list'),
    
    path('detail/<int:id>/<slug:slug>/',imaage_detail,name='detail'),

    path('image/like',image_like,name='like'),

]