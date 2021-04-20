"""pages URL configuration."""

from django.urls import path

from . import views


urlpatterns = [
	# Home page
	path('', views.index, name='index'),
	# Help page
	path('help/', views.help, name='help'),
]
