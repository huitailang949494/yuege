from django.contrib import admin
from paper.models import Author, Paper, Paper_Author_Affiliations


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'author_name')


class PaperAdmin(admin.ModelAdmin):
    list_display = ("paper_id", "original_title", "normalized_title",
                    "publish_year", "publish_date", "DOI", "original_venue_name",
                    "normalized_venue_name", "jornal_id", "conference_id", "paper_rank")


class Paper_Author_AffiliationsAdmin(admin.ModelAdmin):
    list_display = ("paper", "author", "affiliation_id",
                    "original_affiliation_name", "normalized_affiliation_name",
                    "author_sequence_number")

admin.site.register(Author, AuthorAdmin)
admin.site.register(Paper, PaperAdmin)
admin.site.register(Paper_Author_Affiliations, Paper_Author_AffiliationsAdmin)
