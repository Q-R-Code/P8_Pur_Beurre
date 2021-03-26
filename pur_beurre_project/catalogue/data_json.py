import requests

url = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=unique_scans_n&?sort_by=popularity&page_size=200&json=true"
req = requests.get(url)
data = req.json()
prod = data["products"]
i=1
for x in prod:
    try:
        if x["nutriscore_grade"]:
            print(f"true {i}")
        elif not x["nutriscore_grade"]:
            if x["no_nutrition_data"]:
                print(f"PASS DE NUTRI ")
        i+=1
    except:
        pass

"""
for x in range(50):
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
    product = Product(name=name, categories=categories,image_url=image_url, nutriscore_grade=nutriscore_grade,
                      image_nutriments=image_nutrition, barcode=barcode, url=url)
    product.save()
"""
