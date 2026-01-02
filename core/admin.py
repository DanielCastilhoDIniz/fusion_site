from django.contrib import admin
from .models import Service, JobTitle, Employee, FeaturedItem


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'icon', 'active', 'created_at', 'updated_at')
    list_filter = ('active',)
    search_fields = ('service', 'description')


@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'active', 'created_at', 'updated_at')
    list_filter = ('active',)
    search_fields = ('job_title',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'active', 'created_at', 'updated_at')
    list_filter = ('active', 'job_title')
    search_fields = ('name', 'bio')


@admin.register(FeaturedItem)
class FeaturedItemAdmin(admin.ModelAdmin):
    list_display = ('feature', 'active', 'created_at', 'updated_at')
    list_filter = ('active',)
    search_fields = ('feature', 'description')

