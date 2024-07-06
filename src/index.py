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
        return response.json()
    else:
        return None

api_key = '37ae7ff77aa1a4b76c78e816f58ca4a3'
city = 'New York'
weather_data = fetch_weather(api_key, city)

# Initialize Firebase Admin SDK
cred = credentials.Certificate('weatherapp-f12c0-firebase-adminsdk-wjvmx-2d795ba13a.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def store_weather_data(city, weather_data):
    doc_ref = db.collection('weather').document(city)
    doc_ref.set(weather_data)

store_weather_data('New York', weather_data)

ref = db.reference('server/saving-data/fireblog/posts')

print(ref.get)