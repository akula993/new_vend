from django.urls import path

from vend.views import HomeList, AddressDetail, DeviceDetail

urlpatterns = [
    path('', HomeList.as_view(), name='home'),
    path('<slug:address>/', AddressDetail.as_view(), name='address_detail'),
    path('device/<slug:slug>/', DeviceDetail.as_view(), name='device_detail'),
]
