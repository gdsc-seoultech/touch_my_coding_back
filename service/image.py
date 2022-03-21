from urllib import response
from flask import jsonify
import requests
import json

class Image:
    def searchImage(query, per_page, page):
        result = {
            "success": True,
            "data": {
                "results": [
                ]
            }
        }
        url = 'https://unsplash.com/napi/search' # 웹 요청 
        params = {'query':query, 'per_page':per_page, 'page':page}
        
        response = requests.get(url, params=params)
        r = response.json()
        count = (page-1)*20 + 0

        for x in r['photos']['results']:
            u = x['urls']['regular']
            result['data']['results'].append({'id': count, 'url': u})
            count = count + 1
            
        
        return result

Image.searchImage('sky', 20,1)