"""
Admin panel configuration interface
"""
from django.contrib import admin
from etnadust import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    """"""
    fieldsets = [
        [
            None, {
                'fields': (
                    'login',
                )
            }
        ],
    ]

admin.site.site_title = 'Alternative ETNA website'
admin.site.site_header = 'ETNA-stud, student driven alternative school website'
