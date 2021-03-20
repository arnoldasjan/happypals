import pandas as pd
import json

traverse_data = json.load(open('static/traverse.json'))
vertical_data = json.load(open('static/vertical.json'))
overhang_data = json.load(open('static/overhang.json'))

traverse = pd.DataFrame(traverse_data['data']['climbs'])
vertical = pd.DataFrame(vertical_data['data']['climbs'])
overhang = pd.DataFrame(overhang_data['data']['climbs'])

traverse_height_profile = pd.Series(traverse['height_profile'].explode())
traverse_height_profile = traverse_height_profile.reset_index().drop('index', axis=1)

vertical_height_profile = pd.Series(vertical['height_profile'].explode())
vertical_height_profile = vertical_height_profile.reset_index().drop('index', axis=1)

overhang_height_profile = pd.Series(overhang['height_profile'].explode())
overhang_height_profile = overhang_height_profile.reset_index().drop('index', axis=1)

vertical_highest_index = vertical_height_profile.sort_values(by='height_profile', ascending=False).iloc[0].name
vertical_highest_value = vertical_height_profile.sort_values(by='height_profile', ascending=False).iloc[0]['height_profile']

traverse_height_index = traverse_height_profile.sort_values(by='height_profile', ascending=False).iloc[0].name
traverse_height_value = traverse_height_profile.sort_values(by='height_profile', ascending=False).iloc[0]['height_profile']

overhang_height_index = overhang_height_profile.sort_values(by='height_profile', ascending=False).iloc[0].name
overhang_height_value = overhang_height_profile.sort_values(by='height_profile', ascending=False).iloc[0]['height_profile']

traverse_duration = traverse_data['data']['climbs'][0]['duration']
vertical_duration = vertical_data['data']['climbs'][0]['duration']
overhang_duration = overhang_data['data']['climbs'][0]['duration']

traverse_total = len(traverse)
vertical_total = len(vertical)
overhang_total = len(overhang)

traverse_timestamp = traverse_height_index / traverse_total * traverse_duration
vertical_timestamp = vertical_highest_index / vertical_total * vertical_duration
overhang_timestamp = overhang_height_index / overhang_total * overhang_duration

