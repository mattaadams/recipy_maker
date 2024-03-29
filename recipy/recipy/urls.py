"""recipy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="ReciPy API",
        default_version='1.0.0',
        description="API doc of recipy"

    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('recipes.urls')),
    path('', include('recommender.urls')),
    path(
        'api/',
        include(
            [path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
                path('swagger/schema', schema_view.with_ui('swagger', cache_timeout=0),
                     name="swagger-schema"),
                path('recipes/', include('recipes.api.urls'), name='recipes-api'),
                path('users/', include('users.api.urls'), name='users-api'), ]))]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
