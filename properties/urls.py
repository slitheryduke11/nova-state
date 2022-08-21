from django.urls import include, path

from . import views

app_name = 'properties'

urlpatterns = [
    path('<str:property_id>/', views.get_property, name='get_property'),
    path('<str:property_id>/post-contact/', views.post_contact, name='post_contact'),
]
