from django.urls import path
from post.views import post_list,post_create,post_delete,post_edit, post_detail
urlpatterns=[
    path("list/",post_list, name="post-list"),
    path("delete/",post_delete,name="post-delete"),
    path("create/",post_create, name="post-create"),
    path("<int:id>/edit/",post_edit,name="post-edit"),
    path("<int:id>/detail/",post_detail,name="post-detail"),
]
