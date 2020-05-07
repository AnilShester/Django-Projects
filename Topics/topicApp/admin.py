from django.contrib import admin
from .models import Topic, Entry
from users.models import UserProfilePic
# Register your m0dels here.
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(UserProfilePic)

