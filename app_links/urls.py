from django.urls import path

from .views import group_invitation_link_renderer

urlpatterns = [
    path("groups/<uuid:group_id>", group_invitation_link_renderer),
]
