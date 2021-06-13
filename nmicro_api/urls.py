from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="CovAnalytica API",
        default_version='v1',
        description="CovAnalytica for Developers",
        terms_of_service="https://www.covanalytica.herokuapp.com",
        contact=openapi.Contact(email="team@covanalytica.com"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  # <-- Here
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # <-- Here
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('appointments.urls')),
    path('api/v1/', include('cases.urls')),
    path('api/v1/', include('reviews.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



