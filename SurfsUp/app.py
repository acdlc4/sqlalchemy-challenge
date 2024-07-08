# Import the dependencies.
from flask import Flask, jsonify
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#################################################
# Database Setup
#################################################

# Create an engine for the sqlite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Stations    = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
#-----------------------------------------------------------------------------------------------------------------------
# Define what to do when a user hits the index route = "/"
@app.route("/")
def home():
    """List all available api routes."""
    return (f"<b>Welcome to Adrian's Flask Climate API!</b><br/>"
            f"<br/>"

            f"<u>Available Routes:</u><br/>"
            f"/api/v1.0/precipitation<br/>"
            f"/api/v1.0/stations<br/>"
            f"/api/v1.0/tobs<br/>"
            f"/api/v1.0/<i>start-date</i>  <small>(NOTE: Replace '<i>start-date</i>' with a date in yyyy-mm-dd format)</small><br/>"
            f"/api/v1.0/<i>start-date</i>/<i>end-date</i>  <small>(NOTE: Replace '<i>start-date</i>' and '<i>end-date</i>' with dates in yyyy-mm-dd format)</small><br/>"
            f"<br/>"

            f"<u>Examples for <i>start-date</i> and <i>start-date/end-date</i></u>:<br/>"
            f"/api/v1.0/<i>2016-08-23</i> <small>for August 23, 2016</small><br/>"
            f"/api/v1.0/<i>2016-08-23</i>/<i>2017-01-05</i> <small>for the date range from August 23, 2016 through January 5, 2017</small><br/>"
           )

#-----------------------------------------------------------------------------------------------------------------------
# Define what to do when a user hits the index route = "/api/v1.0/precipitation"
@app.route("/api/v1.0/precipitation")
def precip():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all precipitation values for the last 12 months of data"""
    # Query last twelve months of data
    results = session.query(Measurement.date, Measurement.prcp).\
                      filter(Measurement.date >= '2016-08-23').\
                      filter(Measurement.station == 'USC00519281').\
                      order_by(Measurement.date).\
                      all()

    session.close()

    # Convert list of tuples into normal list
    twelve_mos = dict(results)

    return jsonify(twelve_mos)

#-----------------------------------------------------------------------------------------------------------------------
# Define what to do when a user hits the index route = "/api/v1.0/stations"
@app.route("/api/v1.0/stations")
def stations():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    """Return a list of stations from the dataset"""  
    
    # Return a JSON list of stations from the dataset
    results = session.query(Stations.station,
                            Stations.name,
                            Stations.latitude,
                            Stations.longitude,
                            Stations.elevation).\
                      all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return(all_stations)
    
#-----------------------------------------------------------------------------------------------------------------------
# Define what to do when a user hits the index route = "/api/v1.0/tobs"
@app.route("/api/v1.0/tobs")
def temps():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all temperatures from the dataset"""
    # Query last twelve months of data for most active station
    results = session.query(Measurement.tobs).\
                      filter(Measurement.date >= '2016-08-23').\
                      filter(Measurement.station == 'USC00519281').\
                      order_by(Measurement.date).\
                      all()

    session.close()

    # Convert list of tuples into normal list
    twelve_mos_temps = list(np.ravel(results))

    return jsonify(twelve_mos_temps)

#-----------------------------------------------------------------------------------------------------------------------
# Define what to do when a user hits the index route = "/api/v1.0/start-date"
@app.route("/api/v1.0/start-date")
def startdate():

    """Return advisory note and example path to use API"""
    return (f"Please use a web address, such as the following examples to use the API<br/>"
            f"<br/>"
            f"This API provides a list of the minimum temperature, the average temperature, and the<br/>"
            f"maximum temperature for a user-specified start date through the rest of the data<br/>"
            f"<br/>"
            f"Address example for <i>start-date</i>:<br/>"
            f"/api/v1.0/<i>2016-08-23</i> for August 23, 2016<br/>")

 # Define what to do when a user hits the index route = "/api/v1.0/start-date/end-date"
@app.route("/api/v1.0/start-date/end-date")
def startenddate():

    """Return advisory note and example path to use API"""
    return (f"Please use a web address, such as the following examples to use the API<br/>"
            f"<br/>"
            f"This API provides a list of the minimum temperature, the average temperature,<br/>"
            f"and the maximum temperature for a user-specified date range<br/>"
            f"<br/>"
            f"<u>Example for <i>start-date/end-date</i></u>:<br/>"
            f"/api/v1.0/<i>2016-08-23/2017-01-05</i> (for the date range of August 23, 2016 to January 5, 2017)<br/>")

#-----------------------------------------------------------------------------------------------------------------------
# Define what to do when a user hits the index route = "/api/v1.0/<start>"
@app.route("/api/v1.0/<start>")
def startpage(start):
    """Fetch minimum, average, and maximum temperatures for a specified start date in
       the path variable supplied by the user, or a 404 if not."""
    
# Create our session (link) from Python to the DB
    session = Session(engine)
    
# Create query session to calculate temp-min, temp-max, temp-average for a user-input start date
    TMIN = session.query(func.min(Measurement.tobs)).\
                   filter(Measurement.date >= start).\
                   all()
    
    TMAX = session.query(func.max(Measurement.tobs)).\
                   filter(Measurement.date >= start).\
                   all()
    
    TAVG = session.query(func.avg(Measurement.tobs)).\
                   filter(Measurement.date >= start).\
                   all()

# Close our session (link) from Python to the DB    
    session.close()

 # Return JSON list of temp-min, temp-max, temp-average
    min_max_avg = list(np.ravel([TMIN, TMAX, TAVG]))
    return(min_max_avg)

#-----------------------------------------------------------------------------------------------------------------------
# Define what to do when a user hits the index route = "/api/v1.0/<start>/<end>"
@app.route("/api/v1.0/<start>/<end>")
def start_endpage(start, end):
    """Fetch minimum, average, and maximum temperatures for a specified start-date/end-date range
       in the path variable supplied by the user."""
    
# Create our session (link) from Python to the DB
    session = Session(engine)
    
# Create query session to calculate temp-min, temp-max, temp-average for a user-input start-date/end-date
    TMIN = session.query(func.min(Measurement.tobs)).\
                   filter(Measurement.date >= start).\
                   filter(Measurement.date <= end).\
                   all()

    
    TMAX = session.query(func.max(Measurement.tobs)).\
                   filter(Measurement.date >= start).\
                   filter(Measurement.date <= end).\
                   all()

    
    TAVG = session.query(func.avg(Measurement.tobs)).\
                   filter(Measurement.date >= start).\
                   filter(Measurement.date <= end).\
                   all()

# Close our session (link) from Python to the DB    
    session.close()

 # Return JSON list of temp-min, temp-max, temp-average
    min_max_avg = list(np.ravel([TMIN, TMAX, TAVG]))
    return(min_max_avg)

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
# Debugger toggle for terminal set to true/on
if __name__ == "__main__":
    app.run(debug=True)
