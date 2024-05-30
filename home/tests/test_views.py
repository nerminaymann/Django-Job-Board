from django.test import TestCase, Client
from django.urls import reverse
from job.models import Job
import json

class TestViews(TestCase):

    # (1) SETUP CODES
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.filter_category_url = reverse('filter_job_category')


    def Test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')

    def Test_filter_category_GET(self):
        response = self.client.get(self.filter_category_url)

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'job/job_list.html')