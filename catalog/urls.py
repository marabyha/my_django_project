from django.urls import path
from . import views
from django.urls import re_path as url


urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^genres/$', views.GenreListView.as_view(), name='genres'),
    url(r'^genre/(?P<pk>\d+)$', views.GenreDetailView.as_view(), name='genre-detail'),
    url(r'^mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author-create'),
    url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author-update'),
    url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author-delete'),
    url(r'^book/create/$', views.BookCreate.as_view(), name='book-create'),
    url(r'^book/(?P<pk>\d+)/update/$', views.BookUpdate.as_view(), name='book-update'),
    url(r'^book/(?P<pk>\d+)/delete/$', views.BookDelete.as_view(), name='book-delete'),
    url(r'^genres/create/$', views.GenreCreate.as_view(), name='genre-create'),
    url(r'^mybooks/create/', views.UserCreate.as_view(), name='user-create'),
    url(r'^mybooks/(?P<username>\d+)/update/', views.UserUpdate.as_view(), name='user-update'),
]
