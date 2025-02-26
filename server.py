from flask import Flask, Response
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def index():
    return "Hello world"

@app.route("/api/product/all")
def get_products():
    products = [
        {
            "name": "Красные розы",
            "description": "Обычные красные розы 🌹",
            "price": 150,
            "photo": "https://primamediamts.servicecdn.ru/f/main/5030/5029680.jpg?38bb7ffccb21a777293822fae1c8473e"
        },
        {
            "name": "Белые розы",
            "description": "Обычные белые розы 🌹 <- белый",
            "price": 200,
            "photo": "https://funburg.ru/upload/iblock/382/uzpxx2ytmhcl5fjq7xbc8ri075ip47yi/belye_rozy.webp"
        }
    ]
    return Response(json.dumps(products), content_type="application/json") 

def main():
    app.run("localhost", 8000, True)

if __name__ == "__main__":
    main()