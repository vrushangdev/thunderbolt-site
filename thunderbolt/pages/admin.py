from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.
from .models import Roadmap,Sponsors,TeamMembers,Usecase,Advisors



class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ('name','post','image_display',)
    list_display_links = ('post','name','image_display',)
    list_filter = ('name','post',)
    search_fields = ('name','post','description',)
    list_per_page = 25
    def image_display(self,obj):
        img_url = '''<img src="{0}" height="150" />'''.replace('{0}',obj.photo_main.url)
        safe_text= mark_safe(img_url)
        return safe_text
    image_display.allow_tags = True
    image_display.short_description = 'Photos'
class AdvisorsAdmin(admin.ModelAdmin):
    list_display = ('name','post','image_display',)
    list_display_links = ('post','name','image_display',)
    list_filter = ('name','post',)
    search_fields = ('name','post','description',)
    list_per_page = 25
    def image_display(self,obj):
        img_url = '''<img src="{0}" width="150" />'''.replace('{0}',obj.photo_main.url)
        safe_text= mark_safe(img_url)
        return safe_text
    image_display.allow_tags = True
    image_display.short_description = 'Photos'

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
    def image_display(self,obj):
        img_url = '''<img src="{0}" width="150" />'''.replace('{0}',obj.uimg.url)
        safe_text= mark_safe(img_url)
        return safe_text
    image_display.allow_tags = True
    image_display.short_description = 'Photos'

class UsecaseAdmin(admin.ModelAdmin):

    list_display = ('title','desc','image_display',)
    list_display_links = ('title','desc','image_display',)
    list_filter = ('title',)
    search_fields = ('title','desc',)
    list_per_page = 25

    def image_display(self,obj):
        img_url = '''<img src="{0}" width="150" />'''.replace('{0}',obj.uimg.url)
        safe_text= mark_safe(img_url)
        return safe_text
    image_display.allow_tags = True
    image_display.short_description = 'Photos'


admin.site.register(Roadmap,RoadmapAdmin)
admin.site.register(Sponsors,SponsorsAdmin)
admin.site.register(Advisors,AdvisorsAdmin)
admin.site.register(Usecase,UsecaseAdmin)

admin.site.register(TeamMembers,TeamMembersAdmin)