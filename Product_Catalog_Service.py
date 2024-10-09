"""
    Product Catalog Service:
    Styrer listen over tilgængelige produkter, inklusive detaljer såsom navn, beskrivelse, pris og billeder.
    Tilbyder funktionalitet til at søge, filtrere og kategorisere produkter.
"""

from flask import Flask, jsonify, request, make_response
import requests
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

with sqlite3.connect('db.db') as conn:
    cur = conn.cursor()
    cur.execute

db_path = os.getenv('DB_PATH')

def fetch_products():
    response = requests.get(db_path)
    return response.json()

@app.route('/products', methods=['GET'])
def read_all():
    products = fetch_products()
    return jsonify(products)


@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = next((p for p in fetch_products() if p['id'] == id), None)
    if product:
        return jsonify(product)
    else:
        return make_response(jsonify({"error": "Product not found"}), 400)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)