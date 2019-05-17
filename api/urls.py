from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('movies', views.MovieViewSet)


schema_view = get_swagger_view(title='Pastebin API')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('req/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('', schema_view),
]