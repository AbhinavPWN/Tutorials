from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_books/', views.BookCreateView.as_view(), name='create_books'),
    path('details/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.CheckOutListView.as_view(), name='profile'),
]
