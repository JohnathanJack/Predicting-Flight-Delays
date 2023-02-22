import numpy as np
import pandas as pd
import os
import json
import requests


def lat_lon_api(city):
    """
    Returns the JSON response of an API call from position stack

    Parameters: 
        city(string): name/location of interest
    
    Returns:
        JSON response of API call
    """
    url = 'http://api.positionstack.com/v1/forward'
    position_stack_key = os.environ['position_stack_key']
    params = {'query':city,
                'access_key':position_stack_key,
                'limit': 1}
    response = requests.get(url, params=params).json()
    return response



def lat_grabber(df):
    """
    Returns the latitude and longitude in a list from a dataframe containing a specific location

    Parameters:
        df(pandas dataframe)

    Returns:
        List of latitudes and longitudes (floats)
    """
    lat_list = []
    lon_list = []
    for city in df['origin_city_name']:
        response = lat_lon_api(city)
        # print(city)
        # print(response)
        if 'latitude' not in response['data'][0]:
            lat_list.append('None')
        else:
            lat = response['data'][0]['latitude']
            lat_list.append(lat)
        if 'longitude' not in response['data'][0]:
            lon_list.append('None')
        else:
            lon = response['data'][0]['longitude']
            lon_list.append(lon)
    return lat_list,lon_list



def weather_api(lat,lon,start):
    """
    Returns the JSON response of an API call from Open-Meteo

    Parameters: 
        lat(float) : latitude of location
        lon(float): longitude of location
        start(string): specific desired date
    
    Returns:
        JSON response of API call
    """
    url = 'https://archive-api.open-meteo.com/v1/archive'
    params = {'latitude':lat,
                'longitude':lon,
                'start_date':start,
                'end_date':start,
                'hourly':'cloudcover',
                'daily':['rain_sum','snowfall_sum'],
                'timezone': 'America/New_York'
                }
    response = requests.get(url, params=params).json()
    return response



def weather_grabber(data):
    """
    Returns the sunny%,cloud%, average snow fall and average rain fall of a specific date

    Parameters:
        data(pandas dataframe)

    Returns:
        List of cloud%, rainfall(mm),snowfall(mm),sunny% (floats)
    """    
    cloud_list = []
    rain_list = []
    snow_list = []
    sunny_list = []
    for info in data.values:
        date = info[0]
        lat = info[-2]
        lon = info[-1]
        response = weather_api(lat,lon,date)
        cloud = np.mean(response['hourly']['cloudcover'])
        sunny = 100 - cloud
        cloud_list.append(cloud)
        sunny_list.append(sunny)
        rain_list.append(response['daily']['rain_sum'][0])
        snow_list.append(response['daily']['snowfall_sum'][0])
    return cloud_list,rain_list,snow_list,sunny_list







