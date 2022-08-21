import json
import requests
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from local_modules.easybroker_conn import EasyBrokerConnection


def index(request):
	"""Get properties and render the main page."""
	properties_are_cached = ('properties' in request.session) # Check if there is information about the properties in the session cache
	successful_connection = True

	if not properties_are_cached or request.session['properties'] is None:
		easybroker_conn = EasyBrokerConnection()
		request.session['properties'] = easybroker_conn.get_properties()
		successful_connection = (easybroker_conn.status_code == 200)
	
	data = request.session['properties']

	properties_per_page = 15
	page = request.GET.get('page', 1)
	paginator = Paginator(data, properties_per_page)

	try:
		properties = paginator.page(page)
	except PageNotAnInteger:
		properties = paginator.page(1)
	except EmptyPage:
		properties = paginator.page(paginator.num_pages)
	
	return render(request, 'index.html', { 'properties': properties })


def login_view(request):
	"""Redirect to the main page once the session is re-established."""	
	return redirect('index')
