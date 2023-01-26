from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from vend.forms import AddressForm
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
    extra_context = {'title': 'Главная страница'}


class AddressDetail(DetailView):
    model = Address
    template_name = 'vend/address_detail.html'
    # slug_field = 'device'
    slug_url_kwarg = 'address'

# AddressCreate

class AddressCreate(CreateView): # новое изменение
    model = Address
    template_name = 'vend/address_new.html'
    # fields = ['name', 'slug', 'to_rent', 'publish']
    form_class = AddressForm


class AddressUpdate(UpdateView):
    model = Address
    fields = ['name', 'to_rent']
    success_url = reverse_lazy('/')
    template_name = 'vend/address_update.html'
    context_object_name = 'address'
    def form_valid(self, form):
        messages.success(self.request, 'The task was updated successfully.')
        return super(AddressUpdate, self).form_valid(form)


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

    # def get_queryset(self):
    #     address = self.kwargs.get('address_id', '')
    #     q = super().get_queryset()
    #     return q.filter(address__slug=address).select_related('address')
