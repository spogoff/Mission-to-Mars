from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#set flask route for main page
@app.route("/")

#function for PyMongo to connect to mongoDB collection mars and return it in an html template using index.html
def index():
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars=mars)

#set flask route for scrape page
@app.route("/scrape")

# function to scrape all data using scraping code and update it into a Mongo databse
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return "Scraping Successful!"

#run flask
if __name__ == "__main__":
   app.run()