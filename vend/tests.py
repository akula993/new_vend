from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from vend.models import Address


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='admin',
            email='test@email.com',
            password='admin'
        )

        self.address = Address.objects.create(
            name='A good title',
            slug='a_good_title',
            to_rent=1000,
        )

    def test_string_representation(self):
        address = Address(name='A sample title')
        self.assertEqual(str(address), address.name)

    def test_get_absolute_url(self):  # new
        self.assertEqual(self.address.get_absolute_url(), '/address/1/')

    def test_address_content(self):
        self.assertEqual(f'{self.address.name}', 'A good title')
        self.assertEqual(f'{self.address.slug}', 'nice_slug_content')

    def test_address_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice slug content')
        self.assertTemplateUsed(response, 'home.html')

    def test_address_detail_view(self):
        response = self.client.get('/address/1/')
        no_response = self.client.get('/address/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'address_detail.html')

    def test_address_create_view(self):  # new
        response = self.client.address(reverse('address_new'), {
            'name': 'New name',
            'slug': 'new_text',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New name')
        self.assertContains(response, 'new_text')

    def test_address_update_view(self):  # новое
        response = self.client.address(reverse('address_update', args='1'), {
            'name': 'Updated name',
            'slug': 'updated_text',
        })
        self.assertEqual(response.status_code, 302)

    def test_address_delete_view(self):  # новое
        response = self.client.address(
            reverse('address_delete', args='1'))
        self.assertEqual(response.status_code, 302)