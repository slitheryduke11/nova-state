import requests
from django.conf import settings

from local_modules.api_connection import APIConnection



class EasyBrokerConnection(APIConnection):
	"""API class that accesses and works with EasyBroker accounts."""
	

	def __init__(self):
		"""Initialize attributes."""

		super(EasyBrokerConnection, self).__init__()
		self._headers['X-Authorization'] = settings.EASYBROKER_API_KEY


	def get_properties(self):
		"""Return the list of published properties from a EasyBroker account"""
		
		properties = []
		# Url of the first page of the properties
		url = 'https://api.stagingeb.com/v1/properties?page=1&limit=20&search%5Bstatuses%5D%5B%5D=published'
		while url is not None: # Evaluate if there is a new page to request data from
			reply = requests.get(url, headers=self._headers)
			self._status_code = reply.status_code
			# The server accepted the request
			if reply.status_code == requests.codes.ok:
				json_data = reply.json()
				url = json_data['pagination']['next_page'] # Url of the next page
				content = json_data['content']
				properties.extend(content[:]) # Store properties
			# The server could not find the requested content
			elif reply.status_code == requests.codes.not_found:
				properties = None
			# Some other server error
			else:
				properties = None
		reply.close()
		return properties


	def get_property(self, property_id):
		"""Return the detailed information of a property from a EasyBroker account."""
		
		# Url of the property info
		url = 'https://api.stagingeb.com/v1/properties/%s' % property_id
		reply = requests.get(url, headers=self._headers)
		self._status_code = reply.status_code
		# The server accepted the request
		if reply.status_code == requests.codes.ok:
			prop = reply.json() # Store property
		# The server could not find the requested content
		elif reply.status_code == requests.codes.not_found:
			prop = None
		# Some other server error
		else:
			prop = None
		reply.close()
		return prop


	def post_contact(self, name, phone, email, property_id, message, source):
		"""Create or update a new lead in EasyBroker who is interested in the provided property."""

		# Url for the contact request
		url = 'https://api.stagingeb.com/v1/contact_requests'
		json_data = {
			'name': name, 'phone': phone,
			'email': email, 'property_id': property_id,
			'message': message, 'source': source
		}
		reply = requests.post(url, headers=self._headers, json=json_data)
		self._status_code = reply.status_code
		reply.close()


	@property
	def headers(self):
		"""Get headers."""

		return self._headers


	@headers.setter
	def headers(self, new_headers):
		"""Set headers."""
		
		self._headers = new_headers


	@property
	def status_code(self):
		"""Get status_code."""

		return self._status_code


	@status_code.setter
	def status_code(self, new_status):
		"""Set status_code."""
		
		self._status_code = new_status  


	def __str__(self):
		"""Return the status of the last request."""

		if self._status_code is not None:
			string = 'The status code of the last request was:' + str(self._status_code)
		else:
			string = 'No request has been made'
		return string

