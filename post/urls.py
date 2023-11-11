from django.urls import path
from .views import delete_post, update_post
 
app_name="post"
urlpatterns=[
    path ("delete/<int:post_id>", delete_post, name="delete-post"),
    path ("update/<int:post_id>", update_post, name="update-post"),
]