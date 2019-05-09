from django.urls import path
from . import views

app_name="accounts"

urlpatterns = [
    path('', views.list,name="list"),
    path('create/', views.create,name="create"),
    path('update/', views.update,name="update"),
    path('logout/', views.logout,name="logout"),
    path('login/', views.login,name="login"),
    path('delete/', views.delete,name="delete"),
    path('detail/', views.detail,name="detail"),
]
