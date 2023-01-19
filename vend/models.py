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

    def get_sum_all(self):
        address_sum = Address.objects.get(name=self.name)
        device_sum = address_sum.device.all()

        def item(aa=0, *args):
            sum_number = []

            for i in args:
                for a in i:
                    for s in a:
                        sum_number.append(s.number)

            return sum(sum_number)

        if device_sum and not None:

            sum_number_list = []
            for dev_sum in device_sum:
                current_datetime = timezone.now()
                list_date = dev_sum.sensor_set.filter(month__year=current_datetime.year,
                                                      month__month=current_datetime.month)
                sum_number_list.append(list_date)
            sum_number = item(0, sum_number_list) * 10

        else:
            sum_number = 0
        return sum_number


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
