from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSitemap(Sitemap):
    def items(self):
        return ['core:home','core:about']
    def location(self, item):
        return reverse(item)