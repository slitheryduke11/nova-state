from abc import ABC, abstractmethod



class APIConnection(ABC):
	"""Abstract class of an API connection."""
	

	def __init__(self):
		"""Initialize attributes."""
		
		self._headers = {
			'accept': 'application/json',
		}
		self._status_code = None


	@abstractmethod
	def get_properties(self):
		"""Return the list of published properties"""

		pass


	@abstractmethod
	def get_property(self, property_id):
		"""Return the detailed information of a property."""
		
		pass


	@abstractmethod
	def post_contact(self, name, phone, email, property_id, message, source):
		"""Create or update a new lead who is interested in the provided property."""

		pass


	@property
	def headers(self):
		"""Return headers."""

		pass


	@headers.setter
	def headers(self, new_headers):
		"""Set headers."""

		pass


	@property
	def status_code(self):
		"""Return HTTP status code."""

		pass


	@status_code.setter
	def status_code(self, new_status):
		"""Set HTTP status code."""

		pass


	@abstractmethod
	def __str__(self):
		"""Return the status of the last request."""

		pass
