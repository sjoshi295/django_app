import requests
from rest_framework.test import APIClient, APITestCase
from banks.models import BankData, BankName


class ApiTest(APITestCase):

    def setUp(self):
        bank =  BankName.objects.create(
            id=1,
            bank_name='SBI'
        )
        BankData.objects.create(
            bank=bank,
            ifsc='ABCD',
            branch='A',
            address='xyz',
            city='Bangalore',
            district='Bangalore',
            state='Karnataka'
        )
        BankData.objects.create(
            bank=bank,
            ifsc='ABCDE',
            branch='B',
            address='wxyz',
            city='Bangalore',
            district='Bangalore',
            state='Karnataka'
        )

    def get_api_client(self):
        credentials = {
            'username': 'abc',
            'password': 'abcd1234'
        }
        response = requests.post(
            'http://localhost:8000/api/login/',
            data=credentials)
        self.assertEqual(response.status_code, 200)
        cred = response.json()
        access = cred['access']
        print(access)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + access)
        return client

    def test_get_bank_ifsc(self):
        client = self.get_api_client()
        response = client.get(
            'http://localhost:8000/api/banks/ABCD/', format='json')
        self.assertEqual(response.status_code, 200)

    def test_get_banks_city(self):
        client = self.get_api_client()
        response = client.get(
            'http://localhost:8000/api/banks/SBI/Bangalore/', format='json')
        self.assertEqual(response.status_code, 200)
