"""garud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from umesh.sitemaps import DomesticSitemap, InternationalSitemap, HotelSitemap

sitemaps = {
    'domestic' : DomesticSitemap, 'InternationalSitemap' : InternationalSitemap, 'HotelSitemap' : HotelSitemap
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, { 'sitemaps' : sitemaps}),
    path('', include('umesh.urls', namespace = 'umesh')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('contact.urls', namespace = 'contact')),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
