from django.contrib import admin

# Register your models here.
from .models import Roadmap,Sponsors,TeamMembers,Usecase,Advisors

admin.site.register(Usecase)


class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ('name','post')
    list_display_links = ('post','name')
    list_filter = ('name','post',)
    search_fields = ('name','post','description',)
    list_per_page = 25
class AdvisorsAdmin(admin.ModelAdmin):
    list_display = ('name','post')
    list_display_links = ('post','name')
    list_filter = ('name','post',)
    search_fields = ('name','post','description',)
    list_per_page = 25

class RoadmapAdmin(admin.ModelAdmin):
    list_display = ('completion_date','details')
    list_display_links = ('completion_date','details',)
    list_filter = ('completion_date',)
    search_fields = ('completion_date','details',)
    list_per_page = 25

class SponsorsAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    list_display_links = ('name','description',)
    list_filter = ('name',)
    search_fields = ('name','description',)
    list_per_page = 25

admin.site.register(Roadmap,RoadmapAdmin)
admin.site.register(Sponsors,SponsorsAdmin)
admin.site.register(Advisors,AdvisorsAdmin)

admin.site.register(TeamMembers,TeamMembersAdmin)