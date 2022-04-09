from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet)
router.register('', PostViewSet)



urlpatterns = router.urls

# Using views
# from .views import UserList, UserDetail, PostList, PostDetail

# urlpatterns = [
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>', UserDetail.as_view()),
#     path('', PostList.as_view()),
#      path('<int:pk>/', PostDetail.as_view()),
# ]