from django.contrib import admin
from contacts.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'listing', 'email')
    list_per_page = 20

admin.site.register(Contact, ContactAdmin)