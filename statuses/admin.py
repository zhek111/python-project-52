from django.contrib import admin
from statuses.models import Statuses


class StatusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Statuses, StatusAdmin)