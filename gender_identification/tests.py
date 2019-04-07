from django.test import TestCase
from django.urls import reverse, resolve
from .views import home

# Create your tests here.
class HomeTests(TestCase):
	def setUp(self):
		#self.board = Board.objects.create(name='Django', description='Django board.')
		url = reverse('home')
		self.response = self.client.get(url)

	def test_home_view_status_code(self):
		url = reverse('home')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)

	def test_home_url_resolves_home_view(self):
		view = resolve('/')
		self.assertEquals(view.func, home)		

class AnalysisResultTests(TestCase):

	def test_result_view_success_status_code(self):
		url = reverse('result')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)

	"""def test_result_view_not_found_status_code(self):
		url = reverse('result')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 404)

	def test_result_url_resolves_result_view(self):
		view = resolve('/result/')
		self.assertEquals(view.func, result)"""

	def test_result_view_contains_link_back_to_homepage(self):
		result_url = reverse('result')
		response = self.client.get(result_url)
		homepage_url = reverse('home')
		self.assertContains(response, 'href="{0}"'.format(homepage_url))

class NewDataTests(TestCase):
    def test_new_data_view_success_status_code(self):
        url = reverse('analyse')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    """def test_new_data_view_not_found_status_code(self):
        url = reverse('analyse')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_data_url_resolves_new_topic_view(self):
        view = resolve('/analyse/')
        self.assertEquals(view.func, new_topic)"""

    def test_new_data_view_contains_link_back_to_home_view(self):
        new_data_url = reverse('result')
        home_url = reverse('home')
        response = self.client.get(new_data_url)
        self.assertContains(response, 'href="{0}"'.format(home_url))