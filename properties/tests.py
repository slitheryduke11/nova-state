from django.test import Client, RequestFactory, TestCase
from unittest.mock import patch

from local_modules.easybroker_conn import EasyBrokerConnection



class TestCalls(TestCase):
	"""Tests for the nova_state and properties apps."""
	

	def setUp(self):
		"""Every test needs a client."""
		self.client = Client()
	

	def test_index_loads(self):
		"""Check that 'index' response is 200 OK."""
		reply = self.client.get('')
		self.assertEqual(reply.status_code, 200)


	def test_index_uses_correct_template(self):
		"""Check that index.html is used by the 'index' function."""
		reply = self.client.get('')
		self.assertTemplateUsed(reply, 'index.html')


	def test_get_property_loads(self):
		"""Check that 'get_property' response is 200 OK when valid public_id"""
		reply = self.client.get('/properties/EB-C6372/')
		self.assertEqual(reply.status_code, 200)


	def test_get_property_redirects(self):
		"""Check that the 'properties' function redirects to 'index' when invalid public_id."""
		reply = self.client.get('/properties/invalid_id/')
		self.assertRedirects(reply, '/')


	def test_login_view_redirects(self):
		"""Check that the 'login_view' function redirects to 'index'."""
		reply = self.client.get('/login/')
		self.assertRedirects(reply, '/')