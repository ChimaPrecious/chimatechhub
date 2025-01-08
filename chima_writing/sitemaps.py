from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSitemap(Sitemap):
    def items(self):
        return ['core:home','core:features','core:pricing']
    def location(self, item):
        return reverse(item)