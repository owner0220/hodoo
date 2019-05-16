from django.urls import path
from . import views

app_name = "movies"


urlpatterns = [
    
    path('', views.main, name='main'),
    path('list', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('<int:id>/',views.detail, name='detail'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/update/',views.update, name='update'),
    path('<int:id>/scores/new/', views.score_new, name='score_new'),
    path('<int:id>/scores/<int:score_new_id>/delete/', views.score_delete, name='score_delete'),
    path('<int:id>/scores/<int:score_id>/update/', views.score_update, name='score_update'),
    path('preticket/',views.preticket, name="preticket"),
    path('<int:id>/like/',views.like, name='like'),
    path('<int:id>/whatched/', views.watched, name='watched'),
    path('like_post/', views.like_post, name='like_post'),
    path('watched_post/', views.watched_post, name='watched_post'),
    path('put_data/<int:year>', views.put_data, name='put_data'),
    path('search/', views.search, name='search'),

    ]