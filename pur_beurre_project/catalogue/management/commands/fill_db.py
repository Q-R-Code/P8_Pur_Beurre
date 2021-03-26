import requests
from django.core.management.base import BaseCommand

from catalogue.models import Product
from django.db import transaction, IntegrityError


class Command(BaseCommand):
    help = "Fill the database with product from API Openfoodfacts"

    def handle(self, *args, **options):
        url = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=unique_scans_n&?sort_by=popularity&page_size=200&json=true"
        req = requests.get(url)
        data = req.json()
        prod = data["products"]
        for x in prod:
            try:
                name = x["product_name"]
                image_url = x["image_url"]
                categories_tag = x["categories_hierarchy"]
                categories = []
                for cat in categories_tag:
                    categories.append(cat[3:])
                nutriscore_grade = x["nutriscore_grade"]
                image_nutrition = x["image_nutrition_url"]
                barcode = x["code"]
                url = x["url"]
                product = Product(name=name, categories=categories, image_url=image_url,
                                nutriscore_grade=nutriscore_grade,
                                image_nutriments=image_nutrition, barcode=barcode, url=url)
                if not Product.objects.filter(name=product.name):
                    product.save()
            except:
                pass
        self.stdout.write('Fill_db : OK!')


"""
        for x in range(200):
            name = data["products"][x].get("product_name_fr")
            image_url = data["products"][x].get("image_url")
            categories_tag = data["products"][x].get("categories_hierarchy")
            categories = []
            for cat in categories_tag:
                categories.append(cat[3:])
            nutriscore_grade = data["products"][x].get("nutriscore_grade")
            image_nutrition = data["products"][x].get("image_nutrition_url")
            barcode = data["products"][x].get("code")
            url = data["products"][x].get("url")
            product = Product(name=name, categories=categories, image_url=image_url, nutriscore_grade=nutriscore_grade,
                              image_nutriments=image_nutrition, barcode=barcode, url=url)
            product.save()      
 """
