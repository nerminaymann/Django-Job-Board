from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve
from job.views import Job_List,Job_Detail,Post_Job

class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):

        # FOR MAKING SURE THAT EVERYTHING IS GOING WELL IN TESTING
        # assert 1 == 2

        url = reverse('Job_List')
        # print(resolve(url))
        self.assertEqual(resolve(url).func, Job_List)

    def test_add_url_is_resolved(self):
        url = reverse('post_job')
        self.assertEqual(resolve(url).func, Post_Job)

    def test_detail_url_is_resolved(self):
        url = reverse('job_detail',args=['slug'])
        self.assertEqual(resolve(url).func,Job_Detail)

    # # IN CASE OF CBV
    # def test_listCBV_url_is_resolved(self):
    #     url = reverse('job-list-api')
    #     self.assertEqual(resolve(url).func.view_class, Job_List)



