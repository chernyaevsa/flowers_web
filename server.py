from flask import Flask, Response, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, text

connection_string = "mysql+pymysql://flowers:123456@192.168.3.120:3306/flowers"
engine = create_engine(connection_string, echo=True)


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def index():
    return "Hello world"

@app.route("/api/product/all")
def get_products():
    with engine.connect() as connection:
        raw_result = connection.execute(text("SELECT * FROM products"))
        result = []
        for r in raw_result.all():
            result.append(r._asdict())
        return jsonify(result)
    return Response(jsonify({"status": "500", "message": "Database is down!"}), status=500)

def main():
    app.run("localhost", 8000, True)

if __name__ == "__main__":
    main()