from django.contrib import admin
from .models import UserProfileModel



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_photo')
    search_fields = ('user__username',)

admin.site.register(UserProfileModel, UserProfileAdmin)