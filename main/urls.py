from django.urls import path

from . import views
app_name = 'app_vladislav_yurenya'

urlpatterns = [
    path('',views.list_author_book ,name = 'all_book_and_authors'),
    path('create_book/',views.CreateBook.as_view(), name='create_book'),
    path('detail_book/<int:pk>/', views.DetailBook.as_view(), name='detail_book'),
    path('delete_book/<int:pk>/', views.DeleteBook.as_view(), name='delete_book'),
    path('update_book/<int:pk>/', views.UpdateBook.as_view(), name='update_book'),
    path('create_author/',views.CreateAuthor.as_view(), name='create_author'),
    path('detail_author/<int:pk>/', views.DetailAuthor.as_view(), name='detail_author'),
    path('delete_author/<int:pk>/', views.DeleteAuthor.as_view(), name='delete_author'),
    path('update_author/<int:pk>/', views.UpdateAuthor.as_view(), name='update_author'),
]