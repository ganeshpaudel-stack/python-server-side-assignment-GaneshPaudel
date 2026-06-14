''' Pharse JSON file representing product details (name, price, quality) and display the details in tabular format.'''

import json
with open("products.json", "w") as file:
    products = [
        {"name": "monitor", "price": 5230, "quality": "High"},
        {"name": "mobilephones", "price": 2200, "quality": "Medium"},
        {"name": "Charger", "price": 5620, "quality": "Low"}
    ]
    json.dump(products, file)
with open("products.json", "r") as file:
    products = json.load(file)
    print(f"{'Name':<15} {'Price':<10} {'Quality':<10}")
    print("-" * 35)
    for product in products:
        print(f"{product['name']:<15} {product['price']:<10} {product['quality']:<10}")