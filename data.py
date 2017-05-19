from collections import OrderedDict


# Creating the time data
def temperature_time_data(data):
    # data structure to store the data
    time_dict = OrderedDict()
    # iterating through the data and retrieving the right time period
    for time_layout in data.iterchildren(tag="time-layout"):
        # getting the layout-key
        time_layout_name = str(getattr(time_layout, "layout-key"))
        # initializing the dict
        time_dict[time_layout_name] = []
        # inserting the time data
        for start_time in time_layout.iterchildren(tag="start-valid-time"):
            time = start_time.text
            time_dict[time_layout_name].append(time)
    # returning the time data
    return time_dict


# Creating the maximum and minimum temperature data
def high_low_data(data, time_dict):
    # data structure to store the data
    high = OrderedDict()
    low = OrderedDict()
    # iterating through the data and retrieving the right time period
    temperature_data = list(data.parameters.iterchildren(tag="temperature"))
    temperature_data = temperature_data[:2]
    for time in temperature_data:
        time_layout = time.get("time-layout")
        temp = None
        if time.get("type") == "maximum":
            temp = high
        elif time.get("type") == "minimum":
            temp = low
        # inserting the temp data
        for time, value in zip(time_dict[time_layout], time.iterchildren(tag="value")):
            if value is not None:
                temp[time] = value
    # returning the temp data
    return high, low


# Creating the wind (sustained and gust) data
def wind_data(data, time_dict):
    # data structure to store the data
    wind_speed_sustained = OrderedDict()
    wind_speed_gust = OrderedDict()
    # iterating through the data and retrieving the right time period
    wind_speed_nodes = list(data.parameters.iterchildren(tag="wind-speed"))
    for node in wind_speed_nodes:
        time_layout = node.get("time-layout")
        temp = None
        if node.get("type") == "sustained":
            temp = wind_speed_sustained
        elif node.get("type") == "gust":
            temp = wind_speed_gust
        # inserting the wind speed data
        for time, value in zip(time_dict[time_layout], node.iterchildren(tag="value")):
            temp[time] = value
    # returning the wind speed data
    return wind_speed_gust, wind_speed_sustained


# Creating the cloud cover percentage data
def amount_of_cloud_cover(data, time_dict):
    # data structure to store the data
    cloud_cover = OrderedDict()
    # iterating through the data and retrieving the right time period
    cloud_cover_vals = list(data.parameters.iterchildren(tag="cloud-amount"))
    for cloud in cloud_cover_vals:
        time_layout = cloud.get("time-layout")
        temp = None
        if cloud.get("type") == "total":
            temp = cloud_cover
        # inserting the cloud cover data
        for time, value in zip(time_dict[time_layout], cloud.iterchildren(tag="value")):
            temp[time] = value
    # returning the cloud cover data
    return cloud_cover


# Creating the weather icons data
def weather_icons_data(data, time_dict):
    # data structure to store the data
    weather_icons = OrderedDict()
    # iterating through the data and retrieving the right time period
    weather_icons_vals = list(data.parameters.iterchildren(tag="conditions-icon"))
    for icon in weather_icons_vals:
        time_layout = icon.get("time-layout")
        temp = None
        if icon.get("type") == "forecast-NWS":
            temp = weather_icons
        # inserting the weather icons data
        for time, value in zip(time_dict[time_layout], icon.iterchildren(tag="icon-link")):
            temp[time] = value
    # returning the weather icons data
    return weather_icons


# Creating the precipitation (Liquid and Snow) data
def liq_snow_precipitation_data(data, time_dict):
    # data structure to store the data
    liq_precipitation = OrderedDict()
    snow_precipitation = OrderedDict()
    # iterating through the data and retrieving the right time period
    snow_precipitation_vals = list(data.parameters.iterchildren(tag="precipitation"))
    for icon in snow_precipitation_vals:
        time_layout = icon.get("time-layout")
        temp = None
        if icon.get("type") == "liquid":
            temp = liq_precipitation
        if icon.get("type") == "snow":
            temp = snow_precipitation
        # inserting the precipitation data
        for time, value in zip(time_dict[time_layout], icon.iterchildren(tag="value")):
            temp[time] = value
    # returning the precipitation data
    return liq_precipitation, snow_precipitation
