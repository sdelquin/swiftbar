from datetime import datetime
from functools import partial

import swiftbarmenu as sbm

from lib import netatmo

MEASURES_TRENDS = {'down': '↓', 'up': '↑'}
NA_VALUE = 'NA'  # value for non-available measurements


def get_measures(device: str):
    ws = netatmo.WeatherStation()
    ws.get_data()
    response = ws.station_by_name()
    if device == 'INDOOR':
        data = response['dashboard_data']
    elif device == 'OUTDOOR':
        data = response['modules'][0]['dashboard_data']
    return data


get_indoor_measures = partial(get_measures, device='INDOOR')
get_outdoor_measures = partial(get_measures, device='OUTDOOR')


def timestamp_to_hour(timestamp: int):
    return datetime.fromtimestamp(timestamp).strftime('%H:%M')


def display_leader_measures(outdoor_data: dict, indoor_data: dict, menu: sbm.Menu):
    outdoor_temp = outdoor_data.get('Temperature', NA_VALUE)
    indoor_temp = indoor_data.get('Temperature', NA_VALUE)
    temp_diff = 'up' if outdoor_temp - indoor_temp > 0 else 'down'
    temp_diff = MEASURES_TRENDS.get(temp_diff, '')

    if outdoor_temp < 15:
        temp_symbol = ':thermometer.snowflake:'
    elif outdoor_temp > 30:
        temp_symbol = ':thermometer.sun:'
    else:
        temp_symbol = ':thermometer:'
    temp_display = f'{temp_symbol} {outdoor_temp}º'.strip()
    menu.add_header(temp_display)

    try:
        last_update = timestamp_to_hour(outdoor_data['time_utc'])
        last_update += 'h'
    except KeyError:
        last_update = NA_VALUE
    last_update_display = f'Last update: {last_update}'
    menu.add_item(last_update_display)


def display_outdoor_measures(data: dict, menu: sbm.Menu):
    temp = data.get('Temperature', NA_VALUE)
    temp_trend = MEASURES_TRENDS.get(data.get('temp_trend', NA_VALUE), '')
    temp_display = f'{temp}º {temp_trend}'.strip()
    menu.add_item(temp_display)

    humidity = data.get('Humidity', NA_VALUE)
    humidity_display = f'H: {humidity}%'
    menu.add_item(humidity_display)

    try:
        when_min_temp = timestamp_to_hour(data['date_min_temp'])
        when_min_temp += 'h'
    except KeyError:
        when_min_temp = NA_VALUE
    min_temp = data.get('min_temp', NA_VALUE)
    min_temp_display = f'↓ {min_temp}º ({when_min_temp})'
    menu.add_item(min_temp_display)

    try:
        when_max_temp = timestamp_to_hour(data['date_max_temp'])
        when_max_temp += 'h'
    except KeyError:
        when_max_temp = NA_VALUE
    max_temp = data.get('max_temp', NA_VALUE)
    max_temp_display = f'↑ {max_temp}º ({when_max_temp})'
    menu.add_item(max_temp_display)


def display_indoor_measures(data: dict, menu: sbm.Menu):
    temp = data.get('Temperature', NA_VALUE)
    temp_trend = MEASURES_TRENDS.get(data.get('temp_trend', NA_VALUE), '')
    temp_display = f'{temp}º {temp_trend}'.strip()
    menu.add_item(temp_display)

    humidity = data.get('Humidity', NA_VALUE)
    humidity_display = f'H: {humidity}%'
    menu.add_item(humidity_display)

    co2 = data.get('CO2', NA_VALUE)
    co2_display = f'CO₂: {co2}ppm'
    menu.add_item(co2_display)

    pressure = data.get('Pressure', NA_VALUE)
    pressure_trend = MEASURES_TRENDS.get(data.get('pressure_trend', NA_VALUE), '')
    pressure_display = f'P: {pressure}mbar {pressure_trend}'.strip()
    menu.add_item(pressure_display)

    noise = data.get('Noise', NA_VALUE)
    noise_display = f'N: {noise}dB'
    menu.add_item(noise_display)

    try:
        when_min_temp = timestamp_to_hour(data['date_min_temp'])
        when_min_temp += 'h'
    except KeyError:
        when_min_temp = NA_VALUE
    min_temp = data.get('min_temp', NA_VALUE)
    min_temp_display = f'↓ {min_temp}º ({when_min_temp})'
    menu.add_item(min_temp_display)

    try:
        when_max_temp = timestamp_to_hour(data['date_max_temp'])
        when_max_temp += 'h'
    except KeyError:
        when_max_temp = NA_VALUE
    max_temp = data.get('max_temp', NA_VALUE)
    max_temp_display = f'↑ {max_temp}º ({when_max_temp})'
    menu.add_item(max_temp_display)
