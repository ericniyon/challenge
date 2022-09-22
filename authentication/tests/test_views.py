
from .test_setup import TestSetUp
from django.urls import reverse

class TestViews(TestSetUp):

    
    def test_cannot_register_without_data(self):
        response = self.client.post(self.register_url)
        
        self.assertEqual(response.status_code, 400)
        
        
    
    def test_can_register_with_data(self):
        response = self.client.post(self.register_url, self.data, format='json')
        self.assertEqual(response.status_code, 200)
        
        

        
    
    def test_cannot_login_with_data(self):
        self.client.post(self.register_url, self.data, format='json')
        response = self.client.post(self.login_url, self.data, format='json')
        self.assertEqual(response.status_code, 200)
        
        

