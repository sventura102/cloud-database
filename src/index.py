import requests
import firebase_admin 
from firebase_admin import credentials, firestore
from firebase_admin import db

# Fetch data from weather api
def fetch_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'imperial' #get temp in farenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Failed to fetch weather data. Status code: {response.status_code}")
        return None

api_key = '37ae7ff77aa1a4b76c78e816f58ca4a3'
city = 'New York'
city1 = 'Reno'
city2 = 'Rexburg'
weather_data = fetch_weather(api_key, city)

# Initialize Firebase Admin SDK
cred = credentials.Certificate('src\weatherapp-f12c0-091b5f31c81f.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Stores weather data for new york in Firestore
def store_weather_data(city, weather_data):
    doc_ref = db.collection('weather').document(city)
    doc_ref = db.collection('weather').document(city1)
    doc_ref = db.collection('weather').document(city2)
    doc_ref.set(weather_data)

store_weather_data('New York', weather_data)
store_weather_data('Reno', weather_data)
store_weather_data('Rexbrug', weather_data)

# References server path in Firestore
ref = db.reference('server/saving-data/fireblog/posts')
# Prints the data at the specified reference path in Firestore.
print(ref.get)