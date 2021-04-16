"""users URL Configuration"""

from django.urls import path, include

from . import views


urlpatterns = [
	# Default auth urls
	path('', include('django.contrib.auth.urls')),

	# Registration/Sign-up page
	path('register/', views.register, name='register'),
]