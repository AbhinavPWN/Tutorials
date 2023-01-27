from django.contrib import admin
from .models import Language, Book, BookInstance, Genre, Author

# Register your models here.
admin.site.register(Language)
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Author)
