
from django.urls import path
from .views import index, all_blogs, single_blog, BlogUpdate,  your_blogs, delete_blog, BlogCreateView, CategoryView

urlpatterns = [
        path('', index, name='blog'),
        path('blogs/', all_blogs, name='all_blogs'),
        path('blogs/<pk>/', single_blog, name='single_blog'),
        path('new-blog/', BlogCreateView.as_view(), name='new_blog'),
        path('new-category/', CategoryView, name='category'),
        path('dashboard/', your_blogs, name='dashboard'),
        path('blogs/<pk>/edit-blog/',BlogUpdate.as_view(), name='edit_blog'),
        path('blogs/<pk>/delete-blog/', delete_blog, name='delete_blog'),
]
 