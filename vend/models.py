from django.db import models
from django.urls import reverse


class Address(models.Model):
    """Адресса в которых стоят аппараты"""
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адресса'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vend:address_detail', kwargs={'address': self.slug})


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
        return reverse('vend:device_detail', kwargs={'id': self.id, 'slug': self.slug})
