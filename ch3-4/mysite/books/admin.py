__author__ = 'maggiehsu99'

from django.contrib import admin
from models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city','country','website')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher', 'publication_date')
    search_fields=('title','publication_date')
    list_filter = ('authors',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
   # fields = ( 'authors','title', 'publisher','publication_date')
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)

admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)







