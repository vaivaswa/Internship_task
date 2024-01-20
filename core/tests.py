from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {'date': '2023-01-01', 'customer_name': 'John Doe'}
        self.invoice = Invoice.objects.create(**self.invoice_data)
        self.invoice_detail_data = {'invoice': self.invoice, 'description': 'Item 1', 'quantity': 2, 'unit_price': 10.0, 'price': 20.0}
        self.invoice_detail = InvoiceDetail.objects.create(**self.invoice_detail_data)
        self.invoice_url = reverse('invoice-list-create')
        self.invoice_detail_url = reverse('invoice-detail-list-create')

    def test_create_invoice(self):
        response = self.client.post(self.invoice_url, data=self.invoice_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_invoice(self):
        response = self.client.get(reverse('invoice-retrieve-update-destroy', args=[self.invoice.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invoice_detail(self):
        response = self.client.post(self.invoice_detail_url, data=self.invoice_detail_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_invoice_detail(self):
        response = self.client.get(reverse('invoice-detail-retrieve-update-destroy', args=[self.invoice_detail.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
