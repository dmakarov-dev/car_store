from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample car data (you would typically use a database)
cars = [
    {"id": 1, "brand": "Toyota", "model": "Camry", "price": 25000},
    {"id": 2, "brand": "Honda", "model": "Civic", "price": 22000},
    {"id": 3, "brand": "Ford", "model": "Mustang", "price": 35000},
]

@app.route('/')
def index():
    return render_template('index.html', cars=cars)

@app.route('/car/<int:car_id>')
def car_detail(car_id):
    car = next((c for c in cars if c["id"] == car_id), None)
    if car:
        return render_template('car_detail.html', car=car)
    else:
        return "Car not found", 404

if __name__ == '__main__':
    app.run(debug=True)
