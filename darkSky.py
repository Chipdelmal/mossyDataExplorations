
import aux
import datetime
import apiKeys as keys

KEY = keys.DKS_API_KEY
date = datetime.datetime(2020, 5, 17)
latlong = (30.047401, -81.546638)

data = aux.requestWeather(latlong, date, KEY)
aux.parseWeatherData(data)
