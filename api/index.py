"""from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'"""

# index.py

from datetime import datetime
#import logging
from flask import Flask, request, render_template
#from replit import db

from apps import weather, bitmap, jokes, news_digest

app = Flask(__name__)

# Suppress GET requests logging
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

def render_home_page():
    with open("templates/index.html", "r") as f:
        page = f.read()
  
    my_bitmap = bitmap.load_bitmap()
    page = page.replace("{my_bitmap}", my_bitmap)
    
    joke = jokes.get_new_joke()
    page = page.replace("{joke}", joke)
    return page

def save_or_fetch_news():
    today = datetime.now().strftime('%Y-%m-%d')
    #if today in db:
    #    return db[today]
    #else:
    #  summary_with_sources = news_digest.main()
    #  db[today] = summary_with_sources
    return "testing the news for now, try again later..."

# ROUTES
@app.route("/")
def home():
    return render_home_page()

@app.route("/bitmap", methods=["GET"])
def get_bitmap():
    return bitmap.load_bitmap()

@app.route("/qr")
def show_qr():
    return render_template("qr-code.html")

@app.route("/joke", methods=["GET"])
def get_joke():
    return jokes.get_new_joke()

@app.route("/news")
def get_news():
    return save_or_fetch_news()

@app.route("/weather", methods=["POST", "GET"])
def weather_page():
    data = request.form
    if 'latitude' in data and 'longitude' in data:
        latitude = data["latitude"]
        longitude = data["longitude"]
        return weather.get_weather(latitude, longitude)
    else:
        return weather.get_location()
