from django.contrib import admin

import TestModel.models as models

class TagInline(admin.TabularInline):
    model = models.Tag
 
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email') # list
    search_fields = ('name', 'email',)
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',),
            'fields': ('age',),
        }]
 
    )

# Register your models here.
admin.site.register(models.Contact, ContactAdmin)
admin.site.register([models.TestTable, models.Tag])