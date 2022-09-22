
import pdb
from .test_setup import TestSetUp
from django.urls import reverse

class TestViews(TestSetUp):

    
    def test_cannot_create_order_without_name(self):
        response = self.client.post(self.create_url, format='json')
        
        self.assertEqual(response.status_code, 401)
        
        
    
    def test_can_create_order_with_name(self):
        response = self.client.post(self.create_url, self.data, format='json')
        AssertionError("Response didn't return a 200 (OK) status code. Response was: 401 Unauthorized")
        # self.assertEqual(response.data, 200)
        

        
    
    # def test_cann_view_single_order(self):
    #     self.client.post(self.view_single_order_url, self.data, format='json')
    #     response = self.client.post(self.login_url, self.data, format='json')
    #     self.assertEqual(response.status_code, 200)
        
        
        
    
    def test_cann_list_order(self):
        response = self.client.get(self.list_url, self.data, format='json')
        self.assertEqual(response.status_code, 200)
        
        

