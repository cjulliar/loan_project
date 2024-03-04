from django.contrib import admin
from .models import User, Company, Request


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "state")

class RequestAdmin(admin.ModelAdmin):
    list_display = ("id", "company", "date", "bank", "term", "gr_appv", "sba_appv", "status")

admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Request, RequestAdmin)