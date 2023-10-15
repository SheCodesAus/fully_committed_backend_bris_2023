from django.contrib import admin
from her_profiles.models import Location, Skills


class LocationAdmin(admin.ModelAdmin):
    pass

class SkillsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)

admin.site.register(Skills, SkillsAdmin)
