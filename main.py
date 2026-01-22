import requests
from bs4 import BeautifulSoup
import csv

URL = "https://books.toscrape.com/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("article", class_="product_pod")

with open("products.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Rating"])

    for product in products:
        name = product.h3.a["title"]
        price = product.find("p", class_="price_color").text
        rating = product.find("p", class_="star-rating")["class"][1]

        writer.writerow([name, price, rating])

print("✅ Data saved to products.csv")
