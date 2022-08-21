from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from local_modules.easybroker_conn import EasyBrokerConnection


def get_property(request, property_id):
	"""Get a specific property and render the property page."""
	easybroker_conn = EasyBrokerConnection()
	prop = easybroker_conn.get_property(property_id)

	successful_connection = (easybroker_conn.status_code == 200)

	return render(request, 'properties/property.html', {
		'property': prop
	})


def post_contact(request, property_id):
	"""Create or update a new lead for the property."""
	easybroker_conn = EasyBrokerConnection()
	easybroker_conn.post_contact(
		name=request.POST['name'], phone=request.POST['phone'],
		email=request.POST['email'], property_id=property_id,
		message=request.POST['message'], source='novastate.com'
	)

	successful_connection = (easybroker_conn.status_code == 200)

	return HttpResponseRedirect(reverse('properties:get_property', args=(property_id, )))