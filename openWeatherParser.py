#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyowm
import apiKeys as keys

owm = pyowm.OWM(keys.OPW_API_KEY)
obs = owm.weather_at_coords(-0.107331,51.503614)
w = obs.get_weather()
print(w)


owm.weather_history_at_place('London,uk')
