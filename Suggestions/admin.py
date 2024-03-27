from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(AcademicSuggestions)
admin.site.register(OutreachSuggetion)
admin.site.register(InfrastructureSuggestion)
admin.site.register(TechnologySuggestion)
admin.site.register(OtherSuggetions)
admin.site.register(Suggestion)