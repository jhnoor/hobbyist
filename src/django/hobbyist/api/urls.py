
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from hobbyist.api import views as api_views
from hobbyist.users import views as user_views
from hobbyist.users import urls as user_urls

router = routers.DefaultRouter()

router.register(r'projects', api_views.ProjectViewSet, base_name='project')
router.register(r'comments', api_views.ProjectCommentViewSet,
                base_name='comment')

router.registry.extend(user_urls.router.registry)

urlpatterns = [
    path('', include(router.urls)),
    path('projects/<int:project_pk>/upvote/', api_views.upvote),
    path('projects/<int:project_pk>/downvote/', api_views.downvote),
    path('projects/<int:project_pk>/comment/', api_views.comment),
    path('users/', include('hobbyist.users.urls')),
    path('auth/register/', user_views.RegistrationAPI.as_view()),
    path('auth/login/', user_views.LoginAPI.as_view()),
    path('auth/user/', user_views.UserAPI.as_view()),
]
