from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class GreeetingTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        response =  self.client.get(reverse('index'))#refrencing url
        self.assertEqual(response.status_code, 200)#expecting response 200
        self.assertContains(response,'Hello')#there should be a word hello
        self.assertTemplateUsed(response,'index.html')#is the page called index.html
 
class GreetingFunctionalityTest(TestCase):
    def test_greeting(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.context['greeting'], 'Hello')