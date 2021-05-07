from django.shortcuts import render
from .models import Book
import datetime

# Create your views here.
def index(request):
    return render(request, 'store/home.html', {
        'page_heading': 'Mystery Books',
        'page_name': 'index'
    })

def store(request):
    books = Book.objects.all()
    book_count = books.count()
    context = {
        'books': books,
        'count': book_count,
        'cardinality_text': 'One' if book_count == 1 else 'More than one',
        'page_heading': 'Welcome to Mystery Bookstore',
        'footer_content': 'Copyright &copy; 2021 Mystery Books',
        'page_name': 'store'
    }
    return render(request, 'store/store.html', context)


def new_book(request):
    if request.method == "POST":
        context = {
                'page_heading': 'Create a Book',
                'page_name': 'new_book',
                'show_form': False,
                'message': 'The book has been created.'
            }  
        try:
            new_book = Book.objects.create(
                title=request.POST.get('title'),
                author=request.POST.get('author'),
                description=request.POST.get('description'),
                publish_date=request.POST.get('publish_date') or datetime.date.today()
            )
            new_book.save()
        except:
            context['message'] = 'There was an error with creating your book, try again!'
            context['show_form'] = True
        return render(request, 'store/new_book.html', context)
    else: # elif request.method == "GET":
        context = {
            'page_heading': 'Create a Book',
            'page_name': 'new_book', 
            'show_form': True
        }
        return render(request, 'store/new_book.html', context)