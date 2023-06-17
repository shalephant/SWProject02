from django.urls import path
from . import views
urlpatterns = [
    path('', views.list_user, name="user-list"),
    path('create/', views.create_user, name="user-create"),
    path('update/<int:pk>', views.update_user, name="user-update"),
    path('delete/<int:pk>', views.delete_user, name="user-delete")
]