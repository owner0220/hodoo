from django.urls import path
from . import views

app_name = "movies"


urlpatterns = [
    
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('<int:id>/',views.detail, name='detail'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('<int:id>/update',views.update, name='update'),
    path('<int:id>/scores/new', views.score_new, name='score_new'),
    path('<int:id>/scores/<int:score_new_id>/delete', views.score_delete, name='score_delete'),
    
    ]