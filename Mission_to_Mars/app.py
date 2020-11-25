# 1. import Flask
from flask import Flask
from scrape_mars.py import scrape
import pymongo

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():

    db = client.marsDatabase
    collection = db.items

    marsData = db.items.find().sort({_id:-1}).limit(1)

    print("Server received request for 'Home' page...")
    return "Welcome to the temporary home page!"


# 4. Define what to do when a user hits the /about route
@app.route("/scrape")
def scrape():
    marsDetails = scrape()    

    db = client.marsDatabase
    collection = db.items

    marsData = {
        'news': marsDetails[0],
        'featuredImage': marsDetails[1],
        'facts': marsDetails[2],
        'hemispheres': marsDetails[3]
    }

    collection.insert_one(marsData)

    return "Scraping data..."


if __name__ == "__main__":
    app.run(debug=True)
