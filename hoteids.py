import requests

import requests
import json

hotelname2 = "saf"

language = 'en'

url = "https://api.worldota.net/api/b2b/v3/search/multicomplete/"

payload1 = {"query": hotelname2,

            "language": language}

payload = json.dumps(payload1)

headers = {

    'Content-Type': 'application/json',
    'Authorization': 'Basic MzIwODo3YmFkZGFlZi00OTIyLTRiMzUtYTczZS01NWEwYWJkYzhlMGM=',
    'Cookie': '__cfduid=d7dd143fabf3187411dfb202f1e448eb61605885792; uid=TfTb8F+35rmz7TYlB6WFAg=='
}

response = requests.request("POST", url, headers=headers, data=payload).json()

print(response)

ids =response['data']['hotels']


idlist=[]
for k in ids:
    ids = k['id']
    print(ids)
    idlist.append(ids)

print(idlist)



# id= response['data']['hotels'][0]['id']
# name=response['data']['hotels'][0]['name']



for id in idlist:
    data = {
        'id':id,
        'language': 'en',

    }

    data = json.dumps(data)

    url = f'https://api.worldota.net/api/b2b/v3/hotel/info/?data={data}'

    payload = {}

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic MzIwODo3YmFkZGFlZi00OTIyLTRiMzUtYTczZS01NWEwYWJkYzhlMGM=',
        'Cookie': '__cfduid=d7dd143fabf3187411dfb202f1e448eb61605885792; uid=TfTb8F+35rmz7TYlB6WFAg=='
    }

    response = requests.request("GET", url, headers=headers, data=payload).json()
    print(response)








#
#
# 'data':{
#     'hotels': [
#         {'id': 'ay_safiya', 'name': 'Ay Safiya', 'region_id': 6131912},
#         {'id': 'amaks_safar_hotel', 'name': 'Amaks Safar Hotel', 'region_id': 1993},
#         {'id': 'guest_house_safar', 'name': 'Guest house Safar', 'region_id': 965825658},
#         {'id': 'ai_safiia', 'name': 'Ai Sofiya Hotel', 'region_id': 6131912},
#         {'id': 'safaric_junction', 'name': 'Safaric Junction', 'region_id': 178019}],
#
#     'regions': [{'id': 3068, 'name': 'Santa Fe, New Mexico', 'type': 'City', 'country_code': 'US'},
#                 {'id': 965846816, 'name': 'Santa Fe, New Mexico', 'type': 'Airport', 'country_code': 'US'},
#                 {'id': 4482, 'name': 'Safranbolu', 'type': 'City', 'country_code': 'TR'},
#                 {'id': 6024039, 'name': 'Safaga', 'type': 'City', 'country_code': 'EG'},
#                 {'id': 177919, 'name': 'Safed', 'type': 'City', 'country_code': 'IL'}]},
#
#     'debug': {'request': {'query': 'saf', 'language': 'en'}, 'key_id': 3208, 'validation_error': None},
#     'status': 'ok', 'error': None
#
# }
#
#
