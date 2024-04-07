from flask import Flask, render_template, request, url_for, redirect
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel_agency.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/europe')
def europe():
    # Query the database to fetch destinations in Europe (assuming Europe has continent_id = 2)
    europe_destinations = Destination.query.filter_by(continent_id=2).all()
    return render_template('europe.html', europe_destinations=europe_destinations)

@app.route('/asia')
def asia():
     # Query the database to fetch destinations in Asia (assuming Asia has continent_id = 1)
     asia_destinations = Destination.query.filter_by(continent_id=1).all()
     return render_template('asia.html', asia_destinations=asia_destinations)

@app.route('/northamerica')
def northamerica():
     northamerica_destinations = Destination.query.filter_by(continent_id=3).all()
     return render_template('northamerica.html', northamerica_destinations=northamerica_destinations)

@app.route('/australia')
def australia():
     australia_destinations = Destination.query.filter_by(continent_id=4).all()
     return render_template('australia.html', australia_destinations=australia_destinations)

# Define models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    bookings = db.relationship('Booking', backref='user', lazy=True)

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    country = db.Column(db.String(100), nullable=False)
    image_path = db.Column(db.String(200), nullable=False)
    continent_id = db.Column(db.Integer, db.ForeignKey('continent.id'), nullable=False)
    bookings = db.relationship('Booking', backref='destination', lazy=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    destination_id = db.Column(db.Integer, db.ForeignKey('destination.id'), nullable=False)
    date_booked = db.Column(db.DateTime, nullable=False)

class Continent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    destinations = db.relationship('Destination', backref='continent', lazy=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to serve the HTML form
@app.route('/add_destination', methods=['GET'])
def add_destination_form():
    return render_template('add_destination.html')

# Route to handle form submission
@app.route('/add_destination', methods=['POST'])
def add_destination():
    # Get form data
    name = request.form['name']
    description = request.form['description']
    price = float(request.form['price'])
    country = request.form['country']
    continent_id = int(request.form['continent'])
    image_file = request.files['image']

    # Save the image file
    image_path = os.path.join('static/images', image_file.filename)
    image_file.save(image_path)

    # Create a new Destination object and add it to the database
    destination = Destination(name=name, description=description, image_path=image_path, price=price, country=country, continent_id=continent_id)
    db.session.add(destination)
    db.session.commit()

    return redirect(url_for('add_destination_form'))

if __name__ == '__main__':
    app.run(port=5001,debug=True)

