from django.db import models
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

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('address_detail', kwargs={'address': self.slug})

    def get_sum(self):
        sum_number = Device.objects.aggregate(total_price=Count('counter'))['total_price']
        n = sum_number * 10
        return n


class Device(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='device')
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
