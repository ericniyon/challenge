
import pdb
from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker

class TestSetUp(APITestCase):
    def setUp(self):
        self.fake = Faker()
        self.create_url = reverse('new_create')
        self.list_url = reverse('list')
        self.view_single_order_url = reverse('detail',args=[1])
        
        self.data = {
            'orderName': self.fake.email().split('@')[0],
            'owner': self.fake.random_int(),
        }
        
        return super().setUp()

    def tearDown(self):
        return super().tearDown()