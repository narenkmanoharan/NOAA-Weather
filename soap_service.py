import urllib.request
import utils
from lxml import objectify
from data import wind_data, high_low_data, temperature_time_data, liq_snow_precipitation_data, amount_of_cloud_cover
from models.forecast import Forecast


# Soap call to the NOAA server to receive the DWML
def get_soap_data(latitude, longitude):
    try:
        parameters = utils.parameter_string_xml()
        # url to be sent to the server
        url = "http://www.weather.gov/forecasts/xml/SOAP_server/ndfdXMLclient.php?lat=%s&lon=%s&product=time-series&%s&Submit=Submit" % (
            latitude, longitude, parameters)
        # receiving the object using urllib
        document = urllib.request.urlopen(url)
        # parsing the XML
        data = objectify.parse(document)
        # the data  object with the attributes
        tree = data.getroot().data
    except:
        raise Exception("Service could not be reached for the given value")
    return tree


# creating the data from the utility data creation function to build the forecast object
def forecast_data(latitude, longitude):
    # Soap call
    data = get_soap_data(latitude, longitude)
    # time data
    time_dict = temperature_time_data(data)
    # temperature data
    high, low = high_low_data(data, time_dict)
    # wind speed data
    wind_speed_gust, wind_speed_sustained = wind_data(data, time_dict)
    # precipitation data
    liquid_precipitation, snow_precipitation = liq_snow_precipitation_data(data, time_dict)
    # Cloud cover data
    cloud_cover = amount_of_cloud_cover(data, time_dict)
    # creating forecast object
    forecast_object = forecast(high, low, wind_speed_gust, cloud_cover, liquid_precipitation, snow_precipitation)
    return forecast_object


# building the forecast object to be sent to the flask app
def forecast(high, low, wind_speed, cloud, liquid_precipitation, snow_precipitation):
    maximum = high.values()
    minimum = low.values()
    wind_speed = wind_speed.values()
    cloud_cover = cloud.values()
    liquid_precipitation = liquid_precipitation.values()
    snow_precipitation = snow_precipitation.values()
    # creating the forecast object
    forecast_obj = Forecast(maximum, minimum, liquid_precipitation, snow_precipitation, cloud_cover, wind_speed)
    return forecast_obj


if __name__ == '__main__':
    lat = 45
    lon = -71
    # lat = int(input("Enter the latitude: "))
    # lon = int(input("Enter the longitude: "))
    forecast_object = forecast_data(lat, lon)
    print(forecast_object)
