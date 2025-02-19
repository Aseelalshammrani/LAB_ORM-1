from django.urls import path
from . import views
app_name = "Blog"
urlpatterns = [
    path('read/',views.read_blog,name='read_blog'),
    path('add/',views.add_blog,name='add_blog'),
    path('detail/<blog_id>/',views.blog_detail,name='blog_detail'),
    path('doesnotexist/',views.not_exist,name='not_exist'),
    path('update/<blog_id>/',views.update_blog,name='update_blog'),
    path('delete/<blog_id>/',views.delete_blog,name='delete_blog')
]
