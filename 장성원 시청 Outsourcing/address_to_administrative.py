import json
import requests
import pandas as pd
from tqdm import tqdm

# Load API keys from the JSON file
def load_api_key(file_path='kakao_map_api_keys.json'):
    with open(file_path) as f:
        api_keys_json = json.load(f)
    return api_keys_json['kakao_rest_api_key']

# Function to retrieve the 행정동 from an 주소
def get_address(address):
    params = {'query': address}
    url = 'https://dapi.kakao.com/v2/local/search/address.json'
    h_name = 'Error'  # Set the initial value to 'Error'

    try:
        json_data = requests.get(url, headers=headers, params=params).json()

        # Handle cases where the 'documents' field is empty in the response
        if json_data['documents']:
            h_name = json_data['documents'][0]['address']['region_3depth_h_name']
        else:
            print(f"No valid data found for address: {address}")
    except Exception as e:
        print(f"Error: {e} | Address: {address}")

    return h_name

# Kakao API settings
api_key = load_api_key()
headers = {"Authorization": f"KakaoAK {api_key}"}

# Read the CSV file with corrected headers
df = pd.read_csv('./address.csv', header=None, names=['상호명', '주소'])

# Extract the part before the first comma and use it for the Kakao API call
df['주소 전처리'] = df['주소'].apply(lambda x: x.split(',')[0] if pd.notnull(x) else 'Error')

# Set the progress bar
tqdm.pandas()

# Add the 행정동 based on the 주소 ('Error' is the default value)
df['행정동'] = df['주소 전처리'].progress_apply(get_address)

# Save the result to a new CSV file
df.to_csv('./address_with_administrative.csv', index=False, encoding='utf-8-sig')
print("작업 완료: 'address_with_administrative.csv' 파일이 생성되었습니다.")