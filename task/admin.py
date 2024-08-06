from django.contrib import admin
from .models import all_the_tasks

class all_the_tasksAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'date_time_target', 'complete')
    search_fields = ('user__username', 'title')
    list_filter = ('date_time_target', 'complete')

admin.site.register(all_the_tasks, all_the_tasksAdmin)

