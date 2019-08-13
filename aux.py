
import requests


def requestWeather(latlong, datetime, KEY):
    urlFormatStr = "https://api.darksky.net/forecast/{}/{},{}"
    baseReq = urlFormatStr.format(KEY, latlong[0], latlong[1])
    dateReq = "{}-{:02}-{:02}".format(
            datetime.year, datetime.month, datetime.day
        )
    url = "{},{}T24:00:00?exclude=hourly&units=si".format(baseReq, dateReq)
    request = requests.get(url)
    if (request.status_code == 200):
        return request.json()
    else:
        return -1


def parseWeatherData(requestJSON):
    return requestJSON["daily"]["data"][0]


def requesteAndParseWeather(latlong, datetime, API_KEY):
    req = requestWeather(latlong, datetime, API_KEY)
    data = parseWeatherData(req)
    nearestStation = req['flags']['nearest-station']
    data['nearest-station'] = nearestStation
    return data
