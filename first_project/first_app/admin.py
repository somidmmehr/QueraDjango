from django.contrib import admin, messages
from django.db.models import F
from .models import *


class BookInLine(admin.StackedInline):
    model = Book.author.through


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
        'is_super',
        'get_books'
    ]
    filter_horizontal = ('books',)
    list_display_links = ('first_name', 'last_name')
    fields = [
        ('first_name', 'last_name'),
        'email',
        'is_super',
    ]
    inlines = [BookInLine]
    #list_editable = ('is_super',)

    def get_books(self, obj):
        return " - ".join([book.name for book in obj.books.all()])

    actions = ['toggle_superiority']

    def toggle_superiority(self, request, queryset):
        updated = queryset.update(is_super=Case(
            When(is_super=1, then=Value(0)),
            When(is_super=0, then=Value(1)),
        ))


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'rate',
        'get_author'
    ]
    search_fields = ['name']
    filter_horizontal = ('author',)
    inlines = [BookInLine]
    actions = ['add_rate']

    def get_author(self, obj):
        return " - ".join([author.first_name + " " + author.last_name for author in obj.author.all()])

    def add_rate(self, request, queryset):
        updated = queryset.update(rate=F('rate') + 1)
        self.message_user(request, f"{updated} rate +1 up!", messages.SUCCESS)

    add_rate.short_description = 'Add +1 to rate'
