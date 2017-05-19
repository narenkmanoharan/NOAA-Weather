import soap_service
from flask import Flask, render_template, request
from models.location import Location

# Starting the flask app
app = Flask(__name__)

# location object to store the latitude and longitude
location = Location()


# Index page
@app.route('/')
def index():
    return render_template('index.html')


# Service page to display the weather
@app.route('/service', methods=['POST'])
def get_service():
    lat = request.form['latitude']
    lon = request.form['longitude']
    location.set_latitude(lat)
    location.set_longitude(lon)
    forecast_obj = soap_service.forecast_data(lat, lon)
    return render_template("temp.html",
                           latitude=lat,
                           longitude=lon,
                           maximum_temp=forecast_obj.max_temp,
                           minimum_temp=forecast_obj.min_temp,
                           wind_speed=forecast_obj.wind_speed,
                           cloud_cover=forecast_obj.cloud_cover,
                           liq_precipitation=forecast_obj.liquid_precipitation,
                           snow_precipitation=forecast_obj.snow_precipitation)


# Refresh page
@app.route('/refresh', methods=['POST'])
def refresh():
    lat = location.get_latitude()
    lon = location.get_longitude()
    forecast_obj = soap_service.forecast_data(lat, lon)
    return render_template("temp.html",
                           latitude=lat,
                           longitude=lon,
                           maximum_temp=forecast_obj.max_temp,
                           minimum_temp=forecast_obj.min_temp,
                           wind_speed=forecast_obj.wind_speed,
                           cloud_cover=forecast_obj.cloud_cover,
                           liq_precipitation=forecast_obj.liquid_precipitation,
                           snow_precipitation=forecast_obj.snow_precipitation)

# Running the application
if __name__ == '__main__':
    app.run()
