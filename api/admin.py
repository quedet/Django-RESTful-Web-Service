from django.contrib import admin

from api.models import Toy

# Register your models here.
@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ['name', 'toy_category', 'was_included_in_home', 'release_date', 'created']
    list_filter = ['toy_category', 'was_included_in_home', 'release_date', 'created', 'updated']

    prepopulated_fields = {'slug': ('name',)}