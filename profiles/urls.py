from django.urls import path
from profiles.views import ProfileEditView
urlpatterns =[
    path("edit/", ProfileEditView.as_view(),name="profile")
]