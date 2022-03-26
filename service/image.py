from ast import keyword
from email import header
import requests
import json
import os # .env 값에서 API_KEY 가져오기 
from dotenv import load_dotenv # 가상 환경에서 환경변수 

class Image:
    def searchImage(query, page):
        image_url_list = []

        requset_url = 'https://unsplash.com/napi/search' # 웹 요청 
        params = {
            'query': query,
            'per_page': 10,
            'page': page
        }
        
        url_response = requests.get(requset_url, params=params).json()["photos"]
    
        total_pages = url_response["total_pages"]
        results = url_response["results"]
        
        if (total_pages >= int(page)): # 정상    
            for i in results:
                urls = i["urls"]["small"]
                image_url_list.append(urls)
            
        server_response = {
            "success": True,
            "total_pages": total_pages,
            "result": image_url_list 
        }    
        
        return server_response

    def getLabel(uri):
        label_list = []

        load_dotenv()
        label = {
            "requests": [
                {
                "image": {
                    "source": {
                    "imageUri": uri
                    }
                },
                "features": [
                    {
                    "type": "LABEL_DETECTION",
                    "maxResults": 5
                    }
                ]
                }
            ]
        }

        json_data = json.dumps(label)
        API_KEY = os.environ.get("API_KEY")

        response = requests.post(f'https://vision.googleapis.com/v1/images:annotate?key={API_KEY}', data=json_data) 
        r = response.json() # json으로 변환 
        labels = r['responses'][0]['labelAnnotations']

        for label in labels:
            label_list.append(label) 

        server_response = {
            "success": True,
            "label": label_list
        }

        return server_response
