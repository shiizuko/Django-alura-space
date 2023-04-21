from django.contrib import admin
from galeria.models import Photography

class ListeningPhotography(admin.ModelAdmin):
    list_display = ("id", "name", "legend", "published")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("category",)
    list_per_page = 10
    list_editable = ("published",)

admin.site.register(Photography, ListeningPhotography)