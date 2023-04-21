from django.contrib import admin
from galeria.models import Photography

class ListeningPhotography(admin.ModelAdmin):
    list_display = ("id", "name", "legend")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("category",)
    list_per_page = 10

admin.site.register(Photography, ListeningPhotography)