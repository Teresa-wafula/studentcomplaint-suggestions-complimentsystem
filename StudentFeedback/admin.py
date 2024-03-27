from django.contrib import admin
from .models import *
# Register your models here.
admin.site.index_title= "Student Affairs"
admin.site.site_header="Student Affairs Admin"

class ComplaintAdmin(admin.ModelAdmin):
   list_display=('category', 'date', 'location', 'description', 'evidence',)
   readonly_fields=('email',)

class OtherComplaintAdmin(admin.ModelAdmin):
    list_display=('category', 'date', 'location', 'description', 'evidence',)
    exclude = ('category',)
    readonly_fields=('email',)

class SexualMisconductComplaintAdmin(admin.ModelAdmin):
    list_display=('category', 'date', 'location', 'description', 'evidence',)
    exclude = ('category',)
    readonly_fields=('email',)

class RapeComplaintAdmin(admin.ModelAdmin):
    list_display=('category', 'date', 'location', 'description', 'evidence',)
    exclude = ('category',)
    readonly_fields=('email',)

class HarassmentComplaintAdmin(admin.ModelAdmin):
    list_display=('category', 'date', 'location', 'description', 'evidence',)
    exclude = ('category',)
    readonly_fields=('email',)


admin.site.register(RapeComplaint,RapeComplaintAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Other, OtherComplaintAdmin)
admin.site.register(SexualMisconductComplaint, SexualMisconductComplaintAdmin)
admin.site.register(HarassmentComplaint, HarassmentComplaintAdmin)
admin.site.register(Student)