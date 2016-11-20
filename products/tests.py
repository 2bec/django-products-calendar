from django.test import TestCase
from products.models import Product, Price

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Jantar Romantico", description="Jantar para 2 (duas) pessoas")
        Product.objects.create(name="Café da tarde", description="Café com panquecas de banana")