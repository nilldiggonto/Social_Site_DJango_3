from django.urls import path
from .views import image_create,imaage_detail

app_name = 'images'
urlpatterns = [
    path('create/',image_create,name='create'),
    path('detail/<int:id>/<slug:slug>/',imaage_detail,name='detail'),
]