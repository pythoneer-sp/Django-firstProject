from django.contrib import admin
from .models import IITPStudent, ItemsReview, Store, Profile
# Register your models here.

class itemsReviewInline(admin.TabularInline):
    model = ItemsReview
    extra = 2

class ItemsVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll')
    inlines = [itemsReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('items',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')

admin.site.register(IITPStudent, ItemsVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Profile, ProfileAdmin)
# admin.site.register(IITPStudent)