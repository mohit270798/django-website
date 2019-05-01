from django.urls import path
from . import views

urlpatterns = [
    # music/
    path('', views.index, name="index"),
    # /music/34
    path('<int:album_id>/', views.detail, name='detail'),
    path('<int:album_id>/favourite', views.favourite, name='favourite'),
]