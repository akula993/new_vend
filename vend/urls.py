from django.urls import path

from vend.views import HomeList, AddressDetail, AddressCreate, DeviceDetail, AddressUpdate

urlpatterns = [
    path('', HomeList.as_view(), name='home'),
    path('new/', AddressCreate.as_view(), name='address_new'),
    path('<slug:address>/', AddressDetail.as_view(), name='address_detail'),
    path('update/<int:pk>/', AddressUpdate.as_view(), name='address_update'),
    path('device/<slug:slug>/', DeviceDetail.as_view(), name='device_detail'),
]
