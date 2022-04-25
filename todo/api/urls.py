
from django.urls import path
from api import views
urlpatterns = [
    path('users/',views.UserList.as_view(),name="users"),
    path('users/<user_id>/',views.UserDetail.as_view(),name="users-detail")
]
