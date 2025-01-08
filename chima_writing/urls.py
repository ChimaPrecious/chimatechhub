
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from chima_writing.sitemaps import StaticSitemap
from django.conf import settings
from django.views.static import serve
from django.urls import re_path
from django.conf.urls.static import static


sitemaps = {
    'static': StaticSitemap,
}
context = {
    'sitemaps': sitemaps
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),

    path('sitemap.xml/', sitemap, context, name="django.contrib.sitemaps.views.sitemap"),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
