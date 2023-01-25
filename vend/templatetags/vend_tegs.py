from django import template
from django.db.models import Sum, Count
from django.db.models.functions import ExtractDay
from django.utils import timezone

from vend.models import Sensor

register = template.Library()


@register.simple_tag
def total_sensor():
    current_datetime = timezone.now()

    # qs = Sensor.objects.filter(month__year=current_datetime.year,
    #                            month__month=current_datetime.month)
    sum_number = Sensor.objects.filter(month__year=current_datetime.year,
                                       month__month=current_datetime.month).aggregate(
        total_price=Sum('number'))['total_price']

    # values = qs.annotate(day=ExtractDay("month")).values("number")
    return sum_number * 10
    # sensor = Sensor.objects.aggregate(a=Sum('number'))['a']
    # return sensor
    # return Post.published.count()
