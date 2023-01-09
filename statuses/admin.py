from django.contrib import admin
from statuses.models import Status


class StatusAdmin(admin.ModelAdmin):
    pass


admin.site.register(Status, StatusAdmin)
