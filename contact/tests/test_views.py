from django.test import TestCase, Client
from django.urls import reverse
from contact.models import Information
import json

class TestViews(TestCase):

    # (1) SETUP CODES
    def setUp(self):
        self.client = Client()
        self.url = reverse('send_messages')

    def Test_send_message_POST(self):
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

