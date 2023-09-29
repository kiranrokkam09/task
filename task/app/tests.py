from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import banks, branches

class BankViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_list_banks(self):
        # Create some test bank objects
        banks.objects.create(name="Bank1", id=1)
        banks.objects.create(name="Bank2", id=2)

        response = self.client.get('/Bank/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

class BranchViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_list_branches(self):
        # Create some test branch objects
        bank = banks.objects.create(name="Bank1", id=1)
        branches.objects.create(ifsc="IFSC1", bank_id=bank, branch="Branch1", address="Address1", city="City1", district="District1", state="State1")

        response = self.client.get('/Branch/?ifsc=IFSC1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
