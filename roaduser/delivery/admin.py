from django.contrib import admin
from delivery.models import Route, PostedItem
from delivery.models import UserProfile

admin.site.register(UserProfile)


class RouteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'rslug':('driverName',)}

class PostedItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'mslug':('itemName',)}


admin.site.register(Route, RouteAdmin)
admin.site.register(PostedItem, PostedItemAdmin)
