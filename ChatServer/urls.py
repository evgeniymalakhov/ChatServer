from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
    path('', include('chat.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
