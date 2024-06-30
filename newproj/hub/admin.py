from django.contrib import admin

from .models import Artist, Vinyl, tag
# Register your models here.

class VinylAdmin(admin.ModelAdmin):
    list_filter = ("title", "artist", "genre", "year")
    list_display = ("title", "artist", "genre", "year")
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Artist)
admin.site.register(Vinyl, VinylAdmin)
admin.site.register(tag)

