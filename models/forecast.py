class Forecast(object):

    # Forecast object with the required fields to be displayed
    def __init__(self, max_temp, min_temp, liquid_precipitation, snow_precipitation, cloud_cover, wind_speed):
        self.wind_speed = wind_speed
        self.cloud_cover = cloud_cover
        self.snow_precipitation = snow_precipitation
        self.liquid_precipitation = liquid_precipitation
        self.min_temp = min_temp
        self.max_temp = max_temp

    # For displaying the weather
    def __str__(self):
        return str(self.max_temp) + str(self.min_temp) + str(self.cloud_cover) + str(self.liquid_precipitation) + \
               str(self.wind_speed) + str(self.snow_precipitation)
