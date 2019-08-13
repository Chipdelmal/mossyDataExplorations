
import aux
import datetime
import apiKeys as keys

catsOfInterest = [
    # Precipitation
    "precipType", "precipProbability", "precipIntensity",
    "precipIntensityMin", "precipIntensityMax", "precipIntensityError",
    # Temperature
    "temperatureLow", "temperatureHigh",
    "temperatureMin", "temperatureMax", "humidity",
    # Wind/Clouds
    "windSpeed", "cloudCover"
    # Other
    "nearest-station"
]

KEY = keys.DKS_API_KEY
date = datetime.datetime(2020, 5, 17)
latlong = (30.047401, -81.546638)

dataPoint = aux.requesteAndParseWeather(latlong, date, KEY)
dataPointCats = [dataPoint[cat] for cat in catsOfInterest]
