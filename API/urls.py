from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from .views import ArtistViewSet, AlbomViewSet, SongViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth import views as auth_views

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapp.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

web_router = DefaultRouter()
web_router.register(r'artists', ArtistViewSet)
web_router.register(r'alboms', AlbomViewSet)
web_router.register(r'songs', SongViewSet)

mobile_router = DefaultRouter()
mobile_router.register(r'artists', ArtistViewSet)
mobile_router.register(r'alboms', AlbomViewSet)
mobile_router.register(r'songs', SongViewSet)

telegram_router = DefaultRouter()
telegram_router.register(r'artists', ArtistViewSet)
telegram_router.register(r'alboms', AlbomViewSet)
telegram_router.register(r'songs', SongViewSet)

urlpatterns = [
    path('api/web/', include(web_router.urls)),
    path('api/mobile/', include(mobile_router.urls)),
    path('api/telegram/', include(telegram_router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
