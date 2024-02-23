from django.contrib import admin
from django.urls import include, path
# from oauth2_provider.views import TokenView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # path('o/token/', TokenView.as_view(), name='token'),
    # path('o/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('o/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('apps/api/v1/authentication/', include('authentication.api.urls')),
]
