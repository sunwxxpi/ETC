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
        
        if 'addresses' in data:
            if data['addresses']:
                return data['addresses'][0]['y'], data['addresses'][0]['x']
            else:
                print(f"No addresses found for: {address}")
                return None, None
        else:
            print(f"Unexpected data format for: {address}")
            print(data)
            return None, None
    else:
        print(f"Request failed for: {address}, Status code: {response.status_code}")
        return None, None
    
# Load API keys from the JSON file
with open('naver_maps_api_keys.json') as f:
    api_keys_json = json.load(f)

# File path to the CSV file containing factory addresses
file_path = './factory.csv'
df = pd.read_csv(file_path, low_memory=False)

# Extract the addresses from the DataFrame
addresses = df['공장대표주소(지번)']

# Dictionary to store coordinates and corresponding row indices
address_coords = {}
for i, address in enumerate(tqdm(addresses, desc='Processing', unit=' Addresses'), start=1):
    lat, lon = get_geocode(address, api_keys=api_keys_json)
    
    if lat and lon:
        key = (float(lat), float(lon))

        if key not in address_coords:
            address_coords[key] = []

        address_coords[key].append(i)

numbering = []

# Create a Folium map centered around the last obtained coordinates
map_ = folium.Map(location=[lat, lon], 
                  zoom_start=15, 
                  tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', 
                  attr='ESRI')

# Add markers to the map for each unique set of coordinates
for key, labels in address_coords.items():
    lat, lon = key
    label = ", ".join(map(str, labels))
    address_list = [addresses.iloc[idx - 1] for idx in labels]
    popup_text = "<br>".join([f"번호: {lbl}, 주소: {addr}" for lbl, addr in zip(labels, address_list)])
    
    folium.Marker(
        [lat, lon],
        popup=folium.Popup(popup_text, max_width=300),
        icon=folium.DivIcon(html=f'<div style="font-size: 14pt; color: yellow">{label}</div>')
    ).add_to(map_)
    
    for idx in labels:
        numbering.append((idx, addresses.iloc[idx - 1]))

# Create a DataFrame with numbering information
numbering_df = pd.DataFrame(numbering, columns=['Number', 'Address']).sort_values(by='Number')
# Add numbering information to the original DataFrame
df['넘버링'] = numbering_df['Number'].values

# Save the updated DataFrame to a new CSV file
df.to_csv('./factory_with_numbering.csv', index=False, encoding='utf-8-sig')
# Save the Folium map to an HTML file
map_.save('./factories_map.html')

print("코드 실행 완료.")