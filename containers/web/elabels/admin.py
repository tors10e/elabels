from django.contrib import admin
from .models import (ApplicationMethod, ApplicationRate, Crop, Label, Ingredient,
                     IngredientAmount, Company, RateUnit)

admin.site.site_header="ELabels"
admin.site.site_title="EPA Labels"


class IngredientAmountInline(admin.TabularInline):
    model = IngredientAmount
    extra = 0


class ApplicationRateInLine(admin.TabularInline):
    model = ApplicationRate
    extra = 0


class LabelAdmin(admin.ModelAdmin):
    fields = ('product_name', 'company')
    inlines = [IngredientAmountInline, ApplicationRateInLine]


admin.site.register(Label, LabelAdmin)
admin.site.register(Ingredient)
admin.site.register(IngredientAmount)
admin.site.register(Company)
admin.site.register(Crop)
admin.site.register(ApplicationMethod)
admin.site.register(RateUnit)
