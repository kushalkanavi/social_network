from django.contrib import admin
from .models import UserProfile, UserFriends

admin.site.register(UserProfile)
admin.site.register(UserFriends)
