# from multiprocessing.connection import Client
from django.test import TestCase, Client
from django.urls import reverse
from job.models import Job
import json

class TestViews(TestCase):

    # (1) SETUP CODES
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('job_list')
        # self.detail_url = reverse('Job_detail', kwargs={'pk':})
        self.detail_url = reverse('Job_detail', args=['slug'])
        self.post_job_url = reverse('post_job')


    def Test_Job_list_GET(self):
        # response = self.client.get(reverse('job_list'))
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'job/job_list.html')

    def Test_Job_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'job/job_detail.html')


    # THERE'S SOME ERROR HERE!
    # def test_pagination_is_four(self):
    #     response = self.client.get(reverse('Job_List'))
    #     self.assertEqual(response.status_code, 200)
    #     # self.assertTrue('is_paginated' in response.context)
    #     # self.assertTrue(response.context['is_paginated'] == True)
    #     self.assertEqual(len(response.context['jobs']), 4)


    # THERE'S SOME ERROR HERE!
    def Test_Job_create_POST(self):
        response = self.client.post(self.post_job_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'job/post_job.html')

    def Test_Job_create_POST_with_no_data(self):
        response = self.client.post(self.post_job_url)
        self.assertEqual(response.status_code,400)










