# Import the dependencies.
from flask import Flask, jsonify



#################################################
# Database Setup
#################################################


# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
# Define what to do when a user hits the index route = "/"
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"


# Define what to do when a user hits the index route = "/api/v1.0/precipitation"
@app.route("/api/v1.0/precipitation")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

# Define what to do when a user hits the index route = "/api/v1.0/stations"
@app.route("/api/v1.0/stations")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

# Define what to do when a user hits the index route = "/api/v1.0/tobs"
@app.route("/api/v1.0/tobs")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

# Define what to do when a user hits the index route = "/api/v1.0/<start>"
@app.route("/api/v1.0/<start>")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

# Define what to do when a user hits the index route = "/api/v1.0/<start>/<end>"
@app.route("/api/v1.0/<start>/<end>")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

# # 1. import Flask
# from flask import Flask

# # 2. Create an app, being sure to pass __name__
# app = Flask(__name__)


# # 3. Define what to do when a user hits the index route
# @app.route("/")
# def home():
#     print("Server received request for 'Home' page...")
#     return "Welcome to my 'Home' page!"


# # 4. Define what to do when a user hits the /about route
# @app.route("/about")
# def about():
#     print("Server received request for 'About' page...")
#     return "Welcome to my 'About' page!"


# if __name__ == "__main__":
#     app.run(debug=True)
