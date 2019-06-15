from django.contrib import admin
from .models import  Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','number','replied')
    list_display_links = ('name', 'email','number',)
    list_editable = ('replied',)
    list_filter = ('name', 'email','replied',)
    search_fields = ('name', 'email', 'number','message',)
    list_per_page = 25
    readonly_fields =('name', 'email', 'number','message','contact_date',)

admin.site.register(Contact,ContactAdmin)