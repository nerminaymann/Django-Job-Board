from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve
from home.views import index,Filter_Job_category

class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):

        url = reverse('home')
        self.assertEqual(resolve(url).func, index)


    def test_filter_category_url_is_resolved(self):
        url = reverse('filter_job_category',args=['category'])
        self.assertEqual(resolve(url).func,Filter_Job_category)