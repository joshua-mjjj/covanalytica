from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from .api import *

router = DefaultRouter()
router.register(r'appointments', AppointmentsViewSet, basename='appointments')

schema_view = get_swagger_view(title='CovAnalytica API')

urlpatterns = [
	path('', include(router.urls)),

]