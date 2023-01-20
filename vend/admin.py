from django.contrib import admin

from vend.models import Address, Device, Sensor, SensorWin


class DeviceInline(admin.TabularInline):
    model = Device


class SensorInline(admin.StackedInline):
    model = Sensor
    # fk_name = None
    extra = 0
    # min_num = None
    # max_num = None
    # template = None
    # verbose_name = None
    # verbose_name_plural = None
    # can_delete = True
    # show_change_link = False
    # classes = None

class SensorWinInline(admin.StackedInline):
    model = SensorWin
    extra = 0


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [DeviceInline, ]


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SensorInline, SensorWinInline, ]
