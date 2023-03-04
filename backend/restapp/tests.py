from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from restapp import views
from rest_framework.test import APIClient

class TestHelpdesk(APITestCase):
	def setUp(self):
		self.factory = APIRequestFactory()
		self.view = views.CustomerList.as_view()
		self.uri = '/api/core/customers/'
		self.client = APIClient()
		
	def test_customer_list(self):
		request = self.factory.get(self.uri)
		response = self.view(request)
		self.assertEqual(response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code))
		
	def test_job_list(self):
		self.uri = '/api/core/jobs/'
		self.view = views.JobViewSet.as_view({'get': 'list'})
		request = self.factory.get(self.uri)
		response = self.view(request)
		self.assertEqual(response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code))
		
	def test_customer_list2(self):
		response = self.client.get(self.uri)
		self.assertEqual(response.status_code, 200,'Expected Response Code 200, received {0} instead.'.format(response.status_code))
		
		
		