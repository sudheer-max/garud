from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Domestic, International, Hotel

class DomesticSitemap(Sitemap):
    def items(self):
        return Domestic.objects.all()


class InternationalSitemap(Sitemap):
    def items(self):
        return International.objects.all()

class HotelSitemap(Sitemap):
    def items(self):
        return Hotel.objects.all()

