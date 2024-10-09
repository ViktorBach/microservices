import sqlite3
import requests


def createTable():
    with sqlite3.connect('db.db') as conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS products
            (id INTEGER PRIMARY KEY , 
            title TEXT, 
            description TEXT,
            category TEXT,
            price TEXT,
            discountPercentage TEXT,
            rating TEXT,
            stock TEXT,
            tags LIST,
            weight TEXT,
            dimensions LIST,
            warrantyInformation TEXT,
            shippingInformation TEXT,
            availabilityStatus LIST,
            reviews LIST,
            returnPolicy TEXT,
            minimumOrderQuantity TEXT,
            meta LIST,
            images LIST,
            thumbnail TEXT,
            )""")
       
    

    conn.executemany('''INSERT INTO products (
            id, 
            title, 
            description,
            category,
            price,
            discountPercentage,
            rating,
            stock,
            tags,
            weight,
            dimensions,
            warrantyInformation,
            shippingInformation,
            availabilityStatus,
            reviews,
            returnPolicy,
            minimumOrderQuantity,
            meta,
            images,
            thumbnail,
             ) VALUES (:title, :description, :category, :price, :discountPercentage, :rating, :stock, :tags, :weight, :dimensions, :warrantyInformation, :shippingInformation, :availabilityStatus, :reviews, returnPolicy, :minimumOrderQuantity, :meta, :images, :thumbnail)''')
    
    conn.commit()
