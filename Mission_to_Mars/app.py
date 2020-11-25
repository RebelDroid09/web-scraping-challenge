# 1. import Flask
from flask import Flask
from scrape_mars.py import scrape

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to the temporary home page!"


# 4. Define what to do when a user hits the /about route
@app.route("/scrape")
def scrape():
    marsDetails = scrape()
    return "Scraping data..."


if __name__ == "__main__":
    app.run(debug=True)
