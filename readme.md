# NOAA Weather App using Flask

### Dependencies

**Install the dependencies using pip**

- Python 3.5.2
- Flask 0.12.1
- Jinja2 2.9.6
- lxml 3.7.3

### Folder Structure

- Models
    - forecast.py - Object used to store the forecast data
    - location.py - Object used to store the Latitude and Longitude data
- Templates
    - index.html - Index page to get the latitude and longitude
    - temp.html - Page to display the weather and refresh the data
- National_Weather_Service.py - Flask application for the weather client
- data.py - Script to create the data for consumption by the forecast object
- soap_service.py - Script to retrieve the XML data using SOAP
- utils.py - utility script to create the parameters

### Script Execution

#### To run the flask app:

1. Install the dependencies using pip
2. Run the flask app by executing the following command - python3 National_Weather_Service.py
3. Then open a web browser and type in the address - http://127.0.0.1:5000/


#### To run the weather client:

1. Install the lxml dependency
2. Run the script - python3 soap_service.py


