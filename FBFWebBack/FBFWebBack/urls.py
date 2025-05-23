from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Djoser base endpoints
    path("api/auth/", include("djoser.urls")),
    
    # JWT endpoints
    path("api/auth/", include("djoser.urls.jwt")),

    # Social auth endpoints (the critical part for Google OAuth2)
    path("api/auth/social/", include("djoser.social.urls")),

    # OpenAPI schema generation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    path("api/millionaire/", include("millionaire.urls")),


    path('api/', include('quiz.urls')),
    
    # your other paths
    path("admin/", admin.site.urls),
    path("api/", include("quiz.urls")),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
