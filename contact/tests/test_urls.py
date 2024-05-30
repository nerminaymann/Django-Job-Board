from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve
from contact.views import Send_Message

class TestUrls(SimpleTestCase):
    def test_message_is_sent_url(self):

        url = reverse('send_messages')
        # print(resolve(url))
        self.assertEqual(resolve(url).func, Send_Message)
