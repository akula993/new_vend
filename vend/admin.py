from django.contrib import admin

from vend.models import Address, Device

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
