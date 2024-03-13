from django.contrib import admin
from .models import *
# Register your models here.
admin.site.index_title= "Student Affairs"
admin.site.site_header="Student Affairs Admin"

admin.site.register(RapeComplaint)
admin.site.register(Complaint)
admin.site.register(BullyingComplaint)
admin.site.register(SexualMisconductComplaint)
admin.site.register(HarassmentComplaint)
admin.site.register(Student)