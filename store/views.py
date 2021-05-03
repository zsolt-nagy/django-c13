from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    return render(request, 'store/home.html')

def store(request):
    book_count = Book.objects.all().count()
    context = {
        'count': book_count,
        'cardinality_text': 'One' if book_count == 1 else 'More than one'
    }
    return render(request, 'store/store.html', context)