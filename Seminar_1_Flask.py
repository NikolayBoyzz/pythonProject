
from flask import Flask, render_template

app = Flask(__name__)

categories_data = {
    "clothes": {
        "name": "Одежда",
        "items": [
            {"name": "Jacket", "description": "Nice coat", "price": 10},
            {"name": "Skirt", "description": "Nice pants", "price": 12},
            {"name": "Socks", "description": "Nice Socks", "price": 5},
        ],
    },
    "tech": {
        "name": "Техника",
        "items": [
            {"name": "Phone", "description": "Nice phone", "price": 700},
            {"name": "Computer", "description": "Nice computer", "price": 1550},
            {"name": "Speaker", "description": "Nice keyboard", "price": 520},
        ],
    },
}


@app.route("/")
def main():
    return render_template("base.html")


@app.route("/categories/<category>/")
def get_category(category):
    if context := categories_data.get(category):
        return render_template("category.html", **context)


if __name__ == "__main__":
    app.run()