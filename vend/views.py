from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from vend.models import Address, Device


def address_list(request):
    address = Address.objects.all()
    context = {
        'address': address,
    }
    return render(request, 'vend/address_list.html', context)


def address_detail(request, addres):
    address = get_object_or_404(Address, slug=addres)
    context = {
        'address': address,
    }
    return render(request, 'vend/address_detail.html')


class HomeList(ListView):
    model = Address
    template_name = 'vend/home.html'
    context_object_name = 'address'


class AddressDetail(DetailView):
    model = Address
    template_name = 'vend/address_detail.html'
    # slug_field = 'device'
    slug_url_kwarg = 'address'

class DeviceDetail(DetailView):
    model = Device
    template_name = 'vend/device_detail.html'
    # slug_field = 'device'
    # slug_url_kwarg = 'device'
    # def get_slug_field(self):
    # def get_queryset(self):
    #     address = self.kwargs.get('address_slug', '')
    #     q = super().get_queryset()
    #     return q.filter(address=address).select_related('device')
    #     # return q.filter(category__slug=category).select_related('address')