from django.contrib import admin
from .models import CarMake, CarModel


# Inline model for CarModel inside CarMake admin
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of blank entries to show

# Admin config for CarMake including CarModel inline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

# Optional: Customize CarModel admin
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'year', 'dealer_id')  # Display fields in admin list view
    search_fields = ('name', 'type')

# Register models with custom admins
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
