from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    # path("users/", views.UserList.as_view(), name="user-list"),
    # path(
    #     "users/<int:pk>/",
    #     views.UserDetail.as_view(),
    #     name="user-detail",
    # ),
    path("", include(router.urls)),
]
