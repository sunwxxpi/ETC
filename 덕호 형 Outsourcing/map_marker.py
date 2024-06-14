import json
import requests
import pandas as pd
import folium
from tqdm import tqdm

# Function to get geocode (latitude, longitude) for a given address using Naver Maps API
def get_geocode(address, api_keys):
    url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    
    client_id = api_keys['client_id']
    client_secret = api_keys['client_secret']
    
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret,
    }
    
    params = {
        "query": address
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        if 'addresses' in data and data['addresses']:
            return data['addresses'][0]['y'], data['addresses'][0]['x']
        else:
            print(f"No addresses found for: {address}")
            return None, None
    else:
        print(f"Request failed for: {address}, Status code: {response.status_code}")
        return None, None

# Load API keys from the JSON file
with open('./naver_maps_api_keys.json') as f:
    api_keys_json = json.load(f)

# File path to the CSV file containing factory addresses
file_path = './factory.csv'
df = pd.read_csv(file_path, low_memory=False)

# Extract the addresses from the DataFrame
addresses = df['공장대표주소(지번)']

# List to store coordinates and their corresponding row indices
address_coords = []
for i, address in enumerate(tqdm(addresses, desc='Processing', unit='Address'), start=1):
    lat, lon = get_geocode(address, api_keys=api_keys_json)
    
    if lat and lon:
        address_coords.append((float(lat), float(lon), i))

# Sort the coordinates from top to bottom, then left to right
sorted_coords = sorted(address_coords, key=lambda x: (-x[0], x[1]))

numbering = []
numbering_map = {}

# Create a Folium map centered around the first obtained coordinates
map_ = folium.Map(location=[sorted_coords[0][0], sorted_coords[0][1]], 
                  zoom_start=15,
                  min_zoom=7,
                  max_zoom=20,
                #   tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}' # Default
                #   tiles='http://mt0.google.com/vt/lyrs=s&hl=ko&x={x}&y={y}&z={z}', # Satellite
                #   tiles='http://mt0.google.com/vt/lyrs=y&hl=ko&x={x}&y={y}&z={z}', # Hybrid
                #   tiles='https://map.pstatic.net/nrs/api/v1/raster/satellite/{z}/{x}/{y}.jpg?version=5.02', # Satelite
                  tiles='https://map.pstatic.net/nrb/styles/satellite/1717723233/{z}/{x}/{y}.png?mt=bg.ol.ts.lko', # Hybrid
                  attr='(NAVER Map) Made by Sunwoo Pi',
                  font_size='1.5rem')

# Dictionary to keep track of which coordinates have been assigned which numbers
coord_number_map = {}
for idx, (lat, lon, original_index) in enumerate(sorted_coords, start=1):
    key = (lat, lon)
    
    if key not in coord_number_map:
        coord_number_map[key] = []
        
    coord_number_map[key].append(idx)
    numbering.append((original_index, idx))
    numbering_map[original_index - 1] = idx

# Add markers to the map for each unique set of coordinates with combined numbering
for (lat, lon), num_list in coord_number_map.items():
    label = "[" + ", ".join(map(str, num_list)) + "]"
    popup_text = "<br>".join([f"{num} : {addresses.iloc[sorted_coords[num-1][2] - 1]}" for num in num_list])
    
    folium.Marker(
        [lat, lon],
        popup=folium.Popup(popup_text, max_width=400),
        icon=folium.DivIcon(html=f'<div style="font-size: 14pt; color: yellow; width: 100px; text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;">{label}</div>')
    ).add_to(map_)

# Add numbering information to the original DataFrame
df['넘버링'] = df.index.map(numbering_map)
# Sort the DataFrame by numbering
df_sorted = df.sort_values(by='넘버링')
# Save the sorted DataFrame to a new CSV file
df_sorted.to_csv('./factory_with_numbering_sorted.csv', index=False, encoding='utf-8-sig')

# Save the Folium map to an HTML file
map_.save('./factory_map.html')

print("코드 실행 완료.")