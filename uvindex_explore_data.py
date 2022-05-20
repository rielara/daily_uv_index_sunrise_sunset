import requests
import json
from requests import Session
import secret
from pprint import pprint as pp
from datetime import datetime
from time import gmtime, strftime
import math

# url containing lon + lat of London, UK
API_url = 'https://api.openuv.io/api/v1/uv?lat=51.52&lng=-0.06&dt=2022-05-24T10:50:52.283Z'
headers = {
    'content-type' : 'application/json',
    'x-access-token' : secret.API_KEY,
    
    }

r = requests.get(API_url, headers = headers)
print(f"Status code: {r.status_code}")


response_dict = r.json()

# Sunrise date + time in human readable format
sunrise_date = datetime.strptime(response_dict['result']['sun_info']['sun_times']['sunrise'], "%Y-%m-%dT%H:%M:%S.%fZ")
readable_sunrise = datetime.strftime(sunrise_date, '%a, %d %b %Y %H:%M:%S +0000')
print (f"Sunrise:{readable_sunrise}")

# UV index for today:
a = response_dict['result']['uv']
uv_rounded = round(a)
print(f"UV index for today: {uv_rounded}")

# Max UV index for today
b = response_dict['result']['uv_max']
uv_max_rounded = round(b)
print(f"Max UV index for today: {uv_max_rounded}")

# Sunset date + time in human readable format
sunset_date = datetime.strptime(response_dict['result']['sun_info']['sun_times']['sunset'], "%Y-%m-%dT%H:%M:%S.%fZ")
readable_sunset = datetime.strftime(sunset_date, '%a, %d %b %Y %H:%M:%S +0000')
print (f"Sunset:{readable_sunset}")



class Solar:

    def __init__(self, token):
        self.apiurl = 'https://api.openuv.io/api/v1/uv'
        self.headers = {'content-type' : 'application/json', 'x-access-token' : token,}
        self.session = Session()
        self.session.headers.update(self.headers)
      
    def getUv(self):
        url = self.apiurl + '/api/v1/uv?lat=51.52&lng=-0.06&dt=2022-05-24T10:50:52.283Z'
        r = self.session.get(url)
        data = r.json()['Solar data']
        return data



solar = Solar(secret.API_KEY)

pp(solar.getUv)

