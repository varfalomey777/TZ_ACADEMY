from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from .models import Book, Author, BookAndAuthor


class CreateBook(CreateView):
    model = Book
    template_name = 'main/create_book.html'
    success_url = reverse_lazy('app_vladislav_yurenya:all_book_and_authors')
    fields = [
        'title',
        'photo',
        'year',
        'genre',
        'pages',
        'author',

    ]

    def form_valid(self, form):
        new = form.save(commit=False)
        form.cleaned_data['name_author']=Author.objects.order_by('fio')
        return super().form_valid(form)



class ListBook(ListView):
    model = Book
    template_name = 'main/all_book.html'

class DetailBook(DetailView):
    model = Book
    template_name = 'main/detail_book.html'

class DeleteBook(DeleteView):
    model = Book
    template_name = 'main/delete_book.html'
    success_url = reverse_lazy('app_vladislav_yurenya:all_book_and_authors')

class UpdateBook(UpdateView):
    model = Book
    template_name = 'main/update_book.html'
    success_url = reverse_lazy('app_vladislav_yurenya:all_book_and_authors')
    fields = [
            'title',
            'photo',
            'year',
            'genre',
            'pages',
            'author',

        ]

class CreateAuthor(CreateView):
    model = Author
    template_name = 'main/create_author.html'
    success_url = reverse_lazy('app_vladislav_yurenya:all_book_and_authors')
    fields = [
        'surname',
        'name',
        'patronymic',
        'birthday',
    ]
    def form_valid(self, form):
        new = form.save(commit=False)
        x = f"{new.surname.capitalize()} {new.name[0].upper()}{'.'}{new.patronymic[0].upper()}{'.'}"
        new.fio = x
        new.save()
        return super().form_valid(form)



class ListAuthor(ListView):
    model = Author
    template_name = 'main/all_author.html'

class DetailAuthor(DetailView):
    model = Author
    template_name = 'main/detail_author.html'

class DeleteAuthor(DeleteView):
    model = Author
    template_name = 'main/delete_author.html'
    success_url = reverse_lazy('app_vladislav_yurenya:all_book_and_authors')

class UpdateAuthor(UpdateView):
    model = Author
    template_name = 'main/update_author.html'
    success_url = reverse_lazy('app_vladislav_yurenya:all_book_and_authors')
    fields = [
        'name',
        'surname',
        'patronymic',
        'birthday',

        ]

def list_author_book(request):
    author = Author.objects.all()
    book = Book.objects.all()
    return render(request,'main/all_book.html',{'author':author,'book':book})

