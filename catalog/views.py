from django.shortcuts import render
from .models import Book, Author, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse


def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_authors': num_authors, 'num_genres': num_genres, 'num_visits': num_visits}
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author


class GenreListView(generic.ListView):
    model = Genre
    paginate_by = 10


class GenreDetailView(generic.DetailView):
    model = Genre
    paginate_by = 10


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name ='catalog/user_detail.html'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.filter(user_loved=self.request.user)


class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'


class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')


class BookCreate(CreateView):
    model = Book
    fields = '__all__'


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'


class BookDelete(DeleteView):
    model = Book
    template_name = 'catalog/book_confrim_delete.html'
    success_url = reverse_lazy('books')


class GenreCreate(CreateView):
    model = Genre
    fields = '__all__'


class UserCreate(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'catalog/user_form.html'

    def get_success_url(self):
        return reverse('index')


class UserUpdate(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
