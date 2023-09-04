from django.contrib import admin
from .models import District, SubArea, Branch, AccountType, Customer, Material


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(SubArea)
class SubAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'district')

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'subarea')

@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'district', 'subarea', 'branch', 'account_type')
    list_filter = ('district', 'subarea', 'branch', 'account_type')
    search_fields = ('name', 'phone_number', 'mail_id', 'district__name', 'subarea__name', 'branch__name')
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address')
        }),
        ('Location and Account', {
            'fields': ('district', 'subarea', 'branch', 'account_type')
        }),
        ('Materials Provided', {
            'fields': ('materials_provide',),
        }),
    )
    filter_horizontal = ('materials_provide',)