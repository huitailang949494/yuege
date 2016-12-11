from django.contrib import admin
from paper.models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'author_name')


admin.site.register(Author, AuthorAdmin)
