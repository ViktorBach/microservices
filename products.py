import requests

Products_Api_Url = 'https://dummyjson.com/products/category/smartphones'

def fetch_products():
    response = requests.get(Products_Api_Url)
    
    if response.status_code == 200:
        full_data = response.json()
        
        products = full_data if isinstance(full_data, list) else full_data.get('products', [])
        
        filtered_products = [
            {
                "brand": product["brand"],
                "category": product["category"],
                "description": product["description"],
                "dimensions": product["dimensions"],
                "id": product["id"],
                "images": product["images"],
                "org_price": product["price"],
                "ddk_price": _calculate_price(product["price"]),
                "tags": product["tags"],
                "thumbnail": product["thumbnail"],
                "title": product["title"],
                "weight": product["weight"]
            }
            for product in products
        ]
        
        return filtered_products
    return []

def _calculate_price(price):
    response = requests.get('https://api.frankfurter.app/latest?base=USD')
    
    if response.status_code == 200:
        data = response.json()
        return round(price * data['rates']['DKK'], 2)
    
    return round(price * 6.8, 2)