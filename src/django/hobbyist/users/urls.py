from django.urls import include, path
from rest_framework import routers
from hobbyist.users import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, base_name='user')

urlpatterns = []
