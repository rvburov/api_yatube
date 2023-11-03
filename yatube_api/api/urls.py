from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)


urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
]
