"""
URL configuration for ssa_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(("users.urls", "users"), namespace="users")),
	path('chipin/', include(("chipin.urls", "chipin"), namespace="chipin")),
]

urlpatterns = [
   path("", views.home, name="home"),
   path('create_group/', views.create_group, name='create_group'),
   path('group/<int:group_id>/', views.group_detail, name='group_detail'),
   path('group/<int:group_id>/invite/', views.invite_users, name='invite_users'),
   path('group/<int:group_id>/accept/', views.accept_invite, name='accept_invite'),
   path('group/<int:group_id>/delete/', views.delete_group, name='delete_group'),
   path('delete-join-request/<int:request_id>/', views.delete_join_request, name='delete_join_request'),
   path('group/<int:group_id>/request-to-join/', views.request_to_join_group, name='request_to_join_group'),
   path('group/<int:group_id>/leave/', views.leave_group, name='leave_group'),
]