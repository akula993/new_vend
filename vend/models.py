from django.db import models
from django.db.models import Sum
from django.urls import reverse
from django.utils import timezone


class Address(models.Model):
    """Адресса в которых стоят аппараты"""
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    to_rent = models.DecimalField('Аренда', max_digits=10, decimal_places=2, blank=True, null=True, )
    publish = models.DateTimeField(default=timezone.now, blank=True, null=True, )

    @classmethod
    def get_default_pk(cls):
        obj, created = cls.objects.get_or_create(name='Без адреса')
        return obj.pk

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('address_detail', kwargs={'address': self.slug})


class Device(models.Model):
    address = models.ForeignKey(Address, on_delete=models.SET_DEFAULT, related_name='device',
                                default=Address.get_default_pk, verbose_name="Адреса")
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Аппарат'
        verbose_name_plural = 'Аппараты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        a = Address.objects.all()
        return reverse('device_detail', kwargs={'slug': self.slug})

    def get_sum(self):
        device_sum = Device.objects.get(name=self.name)
        try:
            last, pre_last = device_sum.sensor_set.order_by('-month')[:2]
            sum_number = (last.number - pre_last.number) * 10
        except ValueError:
            try:
                last, pre_last = device_sum.sensor_set.last(), 0
                sum_number = (last.number) * 10
            except AttributeError:
                sum_number = 0
        return sum_number

    def get_sum_win(self):
        device_sum = Device.objects.get(name=self.name)
        try:
            last, pre_last = device_sum.sensor_win_set.order_by('-month')[:2]
            sum_number = (last.number - pre_last.number)
        except ValueError:
            try:
                last, pre_last = device_sum.sensor_win_set.last(), 0
                sum_number = (last.number)
            except AttributeError:
                sum_number = 0
        return sum_number

    def get_sell(self):
        device_sum = Device.objects.get(name=self.name)
        try:
            last, pre_last = device_sum.sensor_set.order_by('-month')[:2]
            sum = (last.number - pre_last.number) * 10
        except ValueError:
            try:
                last, pre_last = device_sum.sensor_set.last(), 0
                sum = (last.number) * 10
            except AttributeError:
                sum = 0
        sum_number = sum - self.address.to_rent
        return sum_number
