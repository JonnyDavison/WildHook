import unittest
from django.test import TestCase
from django.urls import reverse
from .models import Product, Category
from .views import all_products, product_detail, add_product, edit_product, delete_product

# MODEL TESTING
class CategoryModelTestCase(unittest.TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category',
                                                friendly_name='Friendly Test Category')

    def tearDown(self):
        self.category.delete()

    def test_category_str_method(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_category_friendly_name(self):
        self.assertEqual(self.category.get_friendly_name(), 'Friendly Test Category')

class ProductModelTestCase(unittest.TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            description='Test Description',
            price=10.00,
            label='P',
            tag='N'
        )

    def tearDown(self):
        self.product.delete()
        self.category.delete()

    def test_product_str_method(self):
        self.assertEqual(str(self.product), 'Test Product')

    def test_product_has_sizes_default_false(self):
        self.assertFalse(self.product.has_sizes)

    def test_product_offer_price_null_blank_true(self):
        self.assertIsNone(self.product.offer_price)

    def test_product_label_choices(self):
        label_choices = dict(Product()._meta.get_field('label').choices)
        self.assertIn('primary', label_choices.values())

    def test_product_tag_choices(self):
        tag_choices = dict(Product()._meta.get_field('tag').choices)
        self.assertIn('NEW', tag_choices.values())

if __name__ == '__main__':
    unittest.main()
