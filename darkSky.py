
import datetime
import requests
import apiKeys as keys

KEY = keys.DKS_API_KEY
urlFormatStr = "https://api.darksky.net/forecast/{}/{},{}"

date = datetime.datetime(2020, 5, 17)
(lat, lon) = (30.047401, -81.546638)

BaseURL = urlFormatStr.format(KEY, lat, lon)
dateStr = "{}-{:02}-{:02}".format(date.year, date.month, date.day)
url = "{},{}T12:00:00?exclude=hourly&units=si".format(baseReq, dateReq)
